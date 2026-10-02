from fastapi import APIRouter, HTTPException

from app.schemas.ride import RideCreate, RideOut
from app.services.tariffs import get_ride_fare
from app.services.whatsapp import build_whatsapp_link

router = APIRouter(prefix="/rides", tags=["Transporte"])

# DEMO — almacenamiento en memoria, se reemplaza por PostgreSQL en la Fase 3.
_rides_db: list[dict] = []
_next_id = 1


def _build_whatsapp_message(ride: dict) -> str:
    """Arma el texto del mensaje de WhatsApp para una solicitud de viaje."""
    return (
        "🚗 SOLICITUD DE VIAJE\n\n"
        f"Cliente: {ride['nombre']}\n"
        f"Teléfono: {ride['telefono']}\n"
        f"Origen: {ride['origen']}\n"
        f"Destino: {ride['destino']}\n"
        f"Pasajeros: {ride['pasajeros']}\n"
        f"Fecha: {ride['fecha']}\n"
        f"Hora: {ride['hora']}\n"
        f"Observaciones: {ride['observaciones'] or 'Ninguna'}\n\n"
        f"Tarifa estimada: {ride['tarifa_estimada']}"
    )


@router.post("", response_model=RideOut, status_code=201)
def create_ride(data: RideCreate):
    """
    Crea una nueva solicitud de viaje.

    1. Calcula la tarifa orientativa según origen/destino.
    2. Guarda la solicitud (en memoria, por ahora).
    3. Genera el enlace de WhatsApp con el resumen de la solicitud.
    """
    global _next_id

    tarifa = get_ride_fare(data.origen, data.destino)

    ride = {
        "id": _next_id,
        **data.model_dump(),
        "tarifa_estimada": tarifa,
        "estado": "pendiente",
    }
    _next_id += 1

    mensaje = _build_whatsapp_message(ride)
    ride["whatsapp_link"] = build_whatsapp_link(mensaje)

    _rides_db.append(ride)
    return ride


@router.get("", response_model=list[RideOut])
def list_rides():
    """
    Lista todas las solicitudes de viaje registradas.

    Por ahora no tiene autenticación (eso es la Fase 17) — la usaremos
    para probar el módulo, y más adelante la reutilizará el panel
    administrativo (Fase 12).
    """
    return _rides_db


@router.get("/{ride_id}", response_model=RideOut)
def get_ride(ride_id: int):
    """Obtiene el detalle de una solicitud de viaje por su id."""
    for ride in _rides_db:
        if ride["id"] == ride_id:
            return ride
    raise HTTPException(status_code=404, detail="Solicitud de viaje no encontrada")
