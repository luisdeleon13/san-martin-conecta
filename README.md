# San Martín Conecta

Plataforma web multiservicio (transporte, comida, ferretería, entregas,
plomería y trámites) para San Martín Zapotitlán, Retalhuleu, Guatemala.

Este repositorio se construye **por fases**. Este README se irá
actualizando en cada fase con lo nuevo que agreguemos.

## Estado actual: Fase 2 — Backend FastAPI (módulo de Transporte)

Ya construimos el primer módulo funcional de punta a punta: **Transporte**.
El flujo completo funciona: formulario → API → cálculo de tarifa →
enlace de WhatsApp.

**Importante — esto es temporal, se reemplaza en fases posteriores:**
- Las solicitudes se guardan **en memoria** (se pierden al reiniciar el
  servidor). En la **Fase 3** las movemos a PostgreSQL.

## Estructura de carpetas (actualizada)

```
san-martin-conecta/
├── backend/
│   ├── app/
│   │   ├── main.py               incluye el router de rides
│   │   ├── core/config.py
│   │   ├── routers/
│   │   │   └── rides.py          endpoints del módulo de Transporte
│   │   ├── schemas/
│   │   │   └── ride.py           validación de datos de entrada/salida
│   │   ├── services/
│   │   │   ├── tariffs.py        tarifas DEMO (temporal)
│   │   │   └── whatsapp.py       generador de enlaces wa.me
│   │   ├── models/                (vacío por ahora, Fase 3)
│   │   └── db/                    (vacío por ahora, Fase 3)
│   ├── requirements.txt
│   ├── .env / .env.example
├── frontend/
│   ├── index.html
│   ├── pages/
│   │   └── transporte.html       formulario de solicitud de viaje
│   ├── css/main.css, rides.css
│   ├── js/main.js, rides.js
```



### 2. Ejecuta el backend

```bash
uvicorn app.main:app --reload
```

### 3. Prueba el endpoint desde Swagger

Abre `http://127.0.0.1:8000/docs` — vas a ver el grupo **Transporte**
con tres endpoints: `POST /rides`, `GET /rides`, `GET /rides/{ride_id}`.
Puedes probarlos directamente ahí con el botón "Try it out".


Rutas con tarifa configurada en la demo (para probar el cálculo):
- El Zapote → San Martín = Q25
- El Zapote → San Felipe = Q35
- El Zapote → Ceiba Blanca = Q30
- Cualquier otra combinación → "Cotizar"



