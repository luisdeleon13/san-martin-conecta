San Martín Conecta

Plataforma web multiservicio (transporte, comida, ferretería, entregas,
plomería y trámites) para San Martín Zapotitlán, Retalhuleu, Guatemala.

Este repositorio se construye **por fases**. Este README se irá
actualizando en cada fase con lo nuevo que agreguemos.

## Estado actual: Fase 1 — Configuración del proyecto

En esta fase solo dejamos listo el esqueleto del proyecto y comprobamos
que backend y frontend pueden ejecutarse y comunicarse. Todavía no hay
funcionalidad real (eso empieza en la Fase 2).

## Estructura de carpetas

```
san-martin-conecta/
├── backend/
│   ├── app/
│   │   ├── main.py          punto de entrada de FastAPI
│   │   ├── core/config.py   lectura de variables de entorno
│   │   ├── models/          (vacío por ahora, Fase 3)
│   │   ├── schemas/         (vacío por ahora, Fase 3)
│   │   ├── routers/         (vacío por ahora, Fase 2 en adelante)
│   │   ├── services/        (vacío por ahora)
│   │   └── db/               (vacío por ahora, Fase 3)
│   ├── static/uploads/       fotos subidas (Fase 15 en adelante)
│   ├── requirements.txt
│   ├── .env                  tus valores reales (NO se sube a git)
│   └── .env.example          plantilla (sí se sube a git)
├── frontend/
│   ├── index.html
│   ├── css/main.css
│   ├── js/main.js
│   ├── pages/                (vacío por ahora, Fase 4 en adelante)
│   └── admin/                (vacío por ahora, Fase 12)
├── docs/
└── .gitignore
```


## Instalación paso a paso

### 1. Entra a la carpeta del backend

```bash
cd backend
```

### 2. Crea un entorno virtual de Python

Un entorno virtual evita que las dependencias de este proyecto se mezclen
con otros proyectos de Python que tengas instalados.

```bash
python -m venv venv
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```


### 4. Ejecuta el backend

Desde la carpeta `backend/`, con el entorno virtual activado:

```bash
uvicorn app.main:app --reload
```
