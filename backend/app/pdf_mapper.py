# pdf_mapper.py — mapea nombre del candidato a su archivo PDF

import os

# Directorio donde están los planes de gobierno
base_dir = os.path.dirname(os.path.dirname(__file__))
PDF_DIR = os.path.join(base_dir, "planes_gobierno")

# Mapeo: fragmento del nombre → nombre del archivo
CANDIDATO_PDF_MAP = {
    "acuña": "plan_acuña_cesar.pdf",
    "alvarez loayza": "plan_alvarez_carlos.pdf",
    "atencio": "plan_atencio_ronald.pdf",
    "belaunde llosa": "plan_belaunde_rafael.pdf",
    "belmont": "plan_belmont_ricardo.pdf",
    "caller": "plan_caller_herbert.pdf",
    "carrasco salazar": "plan_carrasco_charlie.pdf",
    "cerrón": "plan_cerron_vladimir.pdf",
    "cerron": "plan_cerron_vladimir.pdf",
    "chiabra": "plan_chiabra_roberto.pdf",
    "chirinos": "plan_chirinos_walter.pdf",
    "diez-canseco": "plan_diezcanseco_francisco.pdf",
    "diezcanseco": "plan_diezcanseco_francisco.pdf",
    "espá": "plan_espa_alfonso.pdf",
    "espa": "plan_espa_alfonso.pdf",
    "fernandez bazan": "plan_fernandez_rosario.pdf",
    "forsyth": "plan_forsyth_george.pdf",
    "fujimori": "plan_fujimori_keiko.pdf",
    "gonzales castillo": "plan_gonzales_alex.pdf",
    "grozo": "plan_grozo_wolfgang.pdf",
    "guevara": "plan_guevara_mesias.pdf",
    "jaico": "plan_jaico_carlos.pdf",
    "jaimes": "plan_jaimes_paul.pdf",
    "lescano": "plan_lescano_yonhy.pdf",
    "lopez chau": "plan_lopez_pablo.pdf",
    "lopez aliaga": "plan_lopez_rafael.pdf",
    "luna galvez": "plan_luna_jose.pdf",
    "masse": "plan_masse_armando.pdf",
    "molinelli": "plan_molinelli_fiorella.pdf",
    "nieto": "plan_nieto_jorge.pdf",
    "olivera": "plan_olivera_luis.pdf",
    "ortiz villano": "plan_ortiz_antonio.pdf",
    "paz de la barra": "plan_pazdelabarra_alvaro.pdf",
    "pazdelabarra": "plan_pazdelabarra_alvaro.pdf",
    "perez tello": "plan_perez_maria.pdf",
    "sanchez palomino": "plan_sanchez_roberto.pdf",
    "valderrama": "plan_valderrama_pitter.pdf",
    "vizcarra cornejo": "plan_vizcarra_mario.pdf",
    "williams": "plan_williams_jose.pdf",
}


def get_pdf_path(nombre_candidato: str) -> str | None:
    """
    Retorna la ruta del PDF del plan de gobierno dado el nombre del candidato.
    """
    nombre_lower = nombre_candidato.lower()
    for clave, archivo in CANDIDATO_PDF_MAP.items():
        if clave in nombre_lower:
            ruta = os.path.join(PDF_DIR, archivo)
            if os.path.exists(ruta):
                return ruta
    return None
