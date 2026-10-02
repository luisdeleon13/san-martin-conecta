from datetime import date, time
from pydantic import BaseModel, Field


class RideCreate(BaseModel):
    """Datos que el cliente envía al solicitar un viaje."""

    nombre: str = Field(..., min_length=2, max_length=100)
    telefono: str = Field(..., min_length=8, max_length=20)
    origen: str = Field(..., min_length=3, max_length=200)
    destino: str = Field(..., min_length=3, max_length=200)
    pasajeros: int = Field(..., ge=1, le=8)
    fecha: date
    hora: time
    observaciones: str | None = Field(default=None, max_length=300)


class RideOut(BaseModel):

    id: int
    nombre: str
    telefono: str
    origen: str
    destino: str
    pasajeros: int
    fecha: date
    hora: time
    observaciones: str | None
    tarifa_estimada: str
    estado: str
    whatsapp_link: str
