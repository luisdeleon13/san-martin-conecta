from urllib.parse import quote

from app.core.config import settings


def build_whatsapp_link(message: str) -> str:
    numero = settings.WHATSAPP_NUMBER
    texto_codificado = quote(message)
    return f"https://wa.me/{numero}?text={texto_codificado}"
