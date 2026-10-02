_DEMO_FARES: dict[tuple[str, str], str] = {
    ("el zapote", "san martin"): "Q25",
    ("el zapote", "san felipe"): "Q35",
    ("el zapote", "ceiba blanca"): "Q30",
}


def get_ride_fare(origen: str, destino: str) -> str:
    clave = (origen.strip().lower(), destino.strip().lower())
    return _DEMO_FARES.get(clave, "Cotizar")
