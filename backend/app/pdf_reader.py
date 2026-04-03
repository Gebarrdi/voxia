# pdf_reader.py — extrae texto de los planes de gobierno en PDF

from pypdf import PdfReader
from app.pdf_mapper import get_pdf_path


def extraer_plan_gobierno(nombre_candidato: str) -> str:
    """Extrae el texto del plan de gobierno de un candidato."""
    ruta = get_pdf_path(nombre_candidato)

    if not ruta:
        return "Plan de gobierno no disponible."

    try:
        reader = PdfReader(ruta)
        texto = ""
        for page in reader.pages:
            texto += page.extract_text() or ""

        # Limitar a 8000 caracteres para no exceder tokens de Claude
        if len(texto) > 8000:
            texto = texto[:8000] + "\n...[resumen truncado]"

        stripped_text = texto.strip()
        return (stripped_text if stripped_text
                else "No se pudo extraer texto del PDF.")

    except Exception as e:
        return f"Error al leer el plan de gobierno: {str(e)}"
