"""
warm_cache.py — Precalentamiento de caché para VoxIA (producción)
=================================================================
Genera análisis de pros/contras y viabilidad para todos los candidatos
en la DB de producción. Los que ya tienen caché se saltan.

Uso:
    cd D:\\VoxIA\\backend
    python warm_cache.py
"""

import asyncio
import httpx
import time
from datetime import datetime

# ── Configuración ────────────────────────────────────────────────────────────
API_URL = "https://voxia-backend-p46z.onrender.com"
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


# ── Llamar endpoint JSON ──────────────────────────────────────────────────────
async def llamar_endpoint(client: httpx.AsyncClient, url: str) -> bool:
    """
    Hace POST al endpoint y espera respuesta JSON.
    Retorna True si terminó correctamente, False si hubo error.
    """
    try:
        resp = await client.post(url)
        if resp.status_code != 200:
            log(f"HTTP {resp.status_code} en {url}", "error")
            return False
        data = resp.json()
        return bool(data)
    except httpx.ReadTimeout:
        log("Timeout — el análisis tardó más de lo esperado", "error")
        return False
    except Exception as e:
        log(f"Error inesperado: {e}", "error")
        return False


# ── Script principal ──────────────────────────────────────────────────────────
async def main():
    separador("VoxIA — Precalentamiento de caché (producción)")
    log(f"API: {API_URL}")
    log(f"Timeout por request: {TIMEOUT_SEGUNDOS}s")
    log(f"Delay entre requests: {DELAY_ENTRE_REQUESTS}s")

    # Verificar que el backend esté activo y obtener candidatos
    try:
        async with httpx.AsyncClient(timeout=15) as client:
            resp = await client.get(f"{API_URL}/api/candidatos/")
            if resp.status_code != 200:
                log("Backend no responde correctamente.", "error")
                return
            candidatos = resp.json()
    except Exception as e:
        log(f"No se puede conectar a {API_URL}: {e}", "error")
        return

    log("Backend activo ✓", "ok")
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
            nombre = candidato["nombre"]
            separador(f"[{i}/{total}] {nombre}  (ID: {candidato['id']})")

            # ── Pros/contras ──────────────────────────────────────────────
            log("Análisis candidato: generando...", "wait")
            inicio = time.time()
            ok = await llamar_endpoint(
                client,
                f"{API_URL}/api/ai/pros-contras/{candidato['id']}"
            )
            elapsed = round(time.time() - inicio, 1)
            if ok:
                if elapsed < 5:
                    log(f"Análisis candidato: ya en caché ({elapsed}s)", "skip")
                    stats["pros_skip"] += 1
                else:
                    log(f"Análisis candidato: generado en {elapsed}s", "ok")
                    stats["pros_ok"] += 1
            else:
                log(f"Análisis candidato: falló ({elapsed}s)", "error")
                stats["pros_error"] += 1

            await asyncio.sleep(DELAY_ENTRE_REQUESTS)

            # ── Viabilidad ────────────────────────────────────────────────
            log("Viabilidad plan: generando...", "wait")
            inicio = time.time()
            ok = await llamar_endpoint(
                client,
                f"{API_URL}/api/ai/viabilidad/{candidato['id']}"
            )
            elapsed = round(time.time() - inicio, 1)
            if ok:
                if elapsed < 5:
                    log(f"Viabilidad plan: ya en caché ({elapsed}s)", "skip")
                    stats["via_skip"] += 1
                else:
                    log(f"Viabilidad plan: generado en {elapsed}s", "ok")
                    stats["via_ok"] += 1
            else:
                log(f"Viabilidad plan: falló ({elapsed}s)", "error")
                stats["via_error"] += 1

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
        log("Algunos fallaron. Vuelve a ejecutar para reintentarlos.", "info")
    else:
        log("¡Caché de producción completamente precalentado!", "ok")


if __name__ == "__main__":
    asyncio.run(main())
