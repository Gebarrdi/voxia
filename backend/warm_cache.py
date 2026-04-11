"""
warm_cache.py — Precalentamiento de caché para VoxIA
=====================================================
Genera análisis de pros/contras y viabilidad para todos los candidatos.
Los que ya tienen caché se saltan. Los que no, se generan secuencialmente.

Uso:
    cd D:\\VoxIA\\backend
    python warm_cache.py

Requisitos:
    - Backend corriendo en http://localhost:8000
    - Variables de entorno configuradas (.env)
"""

import asyncio
import httpx
import time
from datetime import datetime
from app.database import AsyncSessionLocal
from app.models.candidato import Candidato, CacheAnalisis
from sqlalchemy import select

# ── Configuración ────────────────────────────────────────────────────────────
API_URL = "http://localhost:8000"
TIMEOUT_SEGUNDOS = 300       # máximo por request (5 min)
DELAY_ENTRE_REQUESTS = 3     # segundos entre llamadas a la API de Anthropic
DELAY_ENTRE_CANDIDATOS = 5   # segundos entre candidatos


# ── Helpers de consola ───────────────────────────────────────────────────────
def log(msg: str, nivel: str = "info"):
    hora = datetime.now().strftime("%H:%M:%S")
    iconos = {"info": "ℹ️ ", "ok": "✅", "skip": "⏭️ ", "error": "❌", "wait": "⏳"}
    print(f"[{hora}] {iconos.get(nivel, '  ')} {msg}")


def separador(titulo: str = ""):
    linea = "─" * 60
    if titulo:
        print(f"\n{linea}")
        print(f"  {titulo}")
        print(f"{linea}")
    else:
        print(linea)


# ── Consumir stream SSE hasta [DONE] ────────────────────────────────────────
async def consumir_stream(client: httpx.AsyncClient, url: str) -> bool:
    """
    Hace POST al endpoint de streaming y consume todos los chunks.
    Retorna True si terminó correctamente, False si hubo error.
    """
    try:
        async with client.stream("POST", url) as resp:
            if resp.status_code != 200:
                log(f"HTTP {resp.status_code} en {url}", "error")
                return False
            async for line in resp.aiter_lines():
                if line == "data: [DONE]":
                    return True
        return True
    except httpx.ReadTimeout:
        log("Timeout — el análisis tardó más de lo esperado", "error")
        return False
    except Exception as e:
        log(f"Error inesperado: {e}", "error")
        return False


# ── Verificar si ya tiene caché ──────────────────────────────────────────────
async def tiene_cache(db, tipo: str, clave: str) -> bool:
    result = await db.execute(
        select(CacheAnalisis).where(
            CacheAnalisis.tipo == tipo,
            CacheAnalisis.clave == clave
        )
    )
    return result.scalar_one_or_none() is not None


# ── Script principal ─────────────────────────────────────────────────────────
async def main():
    separador("VoxIA — Precalentamiento de caché")
    log(f"API: {API_URL}")
    log(f"Timeout por request: {TIMEOUT_SEGUNDOS}s")
    log(f"Delay entre requests: {DELAY_ENTRE_REQUESTS}s")

    # Verificar que el backend esté activo
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(f"{API_URL}/api/candidatos/")
            if resp.status_code != 200:
                log("Backend no responde correctamente. ¿Está corriendo?", "error")
                return
    except Exception:
        log(f"No se puede conectar a {API_URL}. Inicia el backend primero.", "error")
        return

    log("Backend activo ✓", "ok")

    # Obtener todos los candidatos
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(Candidato).order_by(Candidato.id))
        candidatos = result.scalars().all()

    total = len(candidatos)
    log(f"Total candidatos encontrados: {total}\n")

    # Contadores
    stats = {
        "pros_skip": 0, "pros_ok": 0, "pros_error": 0,
        "via_skip": 0,  "via_ok": 0,  "via_error": 0,
    }

    inicio_total = time.time()

    async with httpx.AsyncClient(timeout=TIMEOUT_SEGUNDOS) as client:
        for i, candidato in enumerate(candidatos, 1):
            clave = str(candidato.id)
            nombre = candidato.nombre
            separador(f"[{i}/{total}] {nombre}  (ID: {candidato.id})")

            async with AsyncSessionLocal() as db:
                cache_pros = await tiene_cache(db, "pros_contras", clave)
                cache_via  = await tiene_cache(db, "viabilidad", clave)

            # ── Pros/contras ──────────────────────────────────────────────
            if cache_pros:
                log("Análisis candidato: ya en caché", "skip")
                stats["pros_skip"] += 1
            else:
                log("Análisis candidato: generando...", "wait")
                inicio = time.time()
                ok = await consumir_stream(
                    client,
                    f"{API_URL}/api/ai/pros-contras/{candidato.id}"
                )
                elapsed = round(time.time() - inicio, 1)
                if ok:
                    log(f"Análisis candidato: generado en {elapsed}s", "ok")
                    stats["pros_ok"] += 1
                else:
                    log(f"Análisis candidato: falló después de {elapsed}s", "error")
                    stats["pros_error"] += 1
                await asyncio.sleep(DELAY_ENTRE_REQUESTS)

            # ── Viabilidad ────────────────────────────────────────────────
            if cache_via:
                log("Viabilidad plan: ya en caché", "skip")
                stats["via_skip"] += 1
            else:
                log("Viabilidad plan: generando...", "wait")
                inicio = time.time()
                ok = await consumir_stream(
                    client,
                    f"{API_URL}/api/ai/viabilidad/{candidato.id}"
                )
                elapsed = round(time.time() - inicio, 1)
                if ok:
                    log(f"Viabilidad plan: generado en {elapsed}s", "ok")
                    stats["via_ok"] += 1
                else:
                    log(f"Viabilidad plan: falló después de {elapsed}s", "error")
                    stats["via_error"] += 1
                await asyncio.sleep(DELAY_ENTRE_REQUESTS)

            # Delay entre candidatos si hubo generación
            if not cache_pros or not cache_via:
                if i < total:
                    log(f"Esperando {DELAY_ENTRE_CANDIDATOS}s antes del siguiente...", "wait")
                    await asyncio.sleep(DELAY_ENTRE_CANDIDATOS)

    # ── Resumen final ─────────────────────────────────────────────────────
    elapsed_total = round(time.time() - inicio_total, 1)
    separador("RESUMEN FINAL")
    print(f"  Tiempo total:          {elapsed_total}s ({round(elapsed_total/60, 1)} min)")
    print(f"  Candidatos procesados: {total}")
    print()
    print(f"  Análisis candidato:")
    print(f"    ⏭️  Ya en caché:  {stats['pros_skip']}")
    print(f"    ✅ Generados:    {stats['pros_ok']}")
    print(f"    ❌ Errores:      {stats['pros_error']}")
    print()
    print(f"  Viabilidad plan:")
    print(f"    ⏭️  Ya en caché:  {stats['via_skip']}")
    print(f"    ✅ Generados:    {stats['via_ok']}")
    print(f"    ❌ Errores:      {stats['via_error']}")
    separador()

    if stats["pros_error"] > 0 or stats["via_error"] > 0:
        log("Algunos análisis fallaron. Vuelve a ejecutar el script para reintentarlos.", "info")
    else:
        log("¡Caché completamente precalentado!", "ok")


if __name__ == "__main__":
    asyncio.run(main())
