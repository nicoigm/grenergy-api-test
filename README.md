# Prueba Técnica – Grenergy

Este proyecto fue desarrollado como parte de una prueba técnica para el cargo IT Specialist en Grenergy. El objetivo es exponer información del proyecto Quillagua a través de una API REST y visualizarla en un dashboard web.

Esto incluye:
- API REST con FastAPI
- Autenticación por API Key
- Configuración por variables de entorno
- Integración con el Coordinador Eléctrico Nacional (CEN)
- Dashboard con Streamlit
- Manejo controlado de errores
- Despliegue en la nube con Render y Streamlit Cloud


## 🚀 Links de acceso rápido
- **API REST:** https://grenergy-api-test.onrender.com/health
- **Swagger:** https://grenergy-api-test.onrender.com/docs
- **Dashboard:** https://grenergy-api-test-wlu8jbkerapppsyadnepaih.streamlit.app/

## Arquitectura

```text
Dashboard (Streamlit)
        │
        ▼
API REST (FastAPI)
        │
        ▼
Autenticación (API Key)
        │
        ▼
Cliente de Integración CEN
        │
        ▼
Servicios Externos del Coordinador Eléctrico Nacional
```

## Estructura del proyecto
```text
grenergy-api-test
│
├── .devcontainer
│
├── backend
│   ├── auth.py
│   ├── cen_client.py
│   ├── config.py
│   ├── main.py
│   └── requirements.txt
│
├── dashboard
│   ├── app.py
│   └── assets
│       └── grenergy_logo.png
│
├── docs
│   ├── dashboard-1.png
│   └── dashboard-2.png
│
├── .gitignore
└── README.md
```

## Endpoints disponibles

### GET /health
Estado de la API. Permite verificar que el servicio se encuentra operativo.

```json
{
  "status": "ok"
}
```

### GET /costo-marginal
Obtiene información de costo marginal para una fecha determinada.

**Parámetros**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| fecha | string | Fecha de consulta |

**Ejemplo**

```http
GET /costo-marginal?fecha=2026-06-18
```

### GET /medidas
Obtiene información de medidas/generación para un rango de fechas.

**Parámetros**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| fecha_inicio | string | Fecha inicial |
| fecha_fin | string | Fecha final |

**Ejemplo**

```http
GET /medidas?fecha_inicio=2026-06-01&fecha_fin=2026-06-18
```

## 🔐 Autenticación
Los endpoints de negocio requieren una API Key en el header de cada solicitud:
X-API-Key: <api-key>

## Instalación y ejecución local

### 1. Crear entorno virtual
```bash
python -m venv venv
```

### 2. Activar entorno virtual
#### Windows
```bash
venv\Scripts\activate
```

#### macOS / Linux
```bash
source venv/bin/activate
```

### 3. Instalar dependencias
Desde la carpeta backend:

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crear un archivo `.env` dentro de la carpeta `backend`:

```env
MY_API_KEY=<tu-api-key>

CEN_API_KEY_SIPUB=<tu-api-key-cen>
CEN_API_KEY_MEDIDAS=<tu-api-key-cen>
```

### 5. Levantar el backend
```bash
uvicorn main:app --reload
```

Swagger local disponible en:

```text
http://127.0.0.1:8000/docs
```

### 6. Levantar el dashboard
Desde la raíz del proyecto:

```bash
streamlit run dashboard/app.py
```

Dashboard local disponible en:

```text
http://localhost:8501
```

## Manejo de errores
La aplicacion implementa un manejo controlado de errores provinientes de servicios externos. Cuando la integación con CEN no responde correctamente, la API devuelve respuestas controladas para evitar fallas en backend y en el dashboard.
json{
  "source": "CEN",
  "status": 403,
  "error": "Authentication parameters missing"
}

## ⚠️ Análisis de la integración con el CEN
La integración fue implementada siguiendo la documentación Swagger oficial del CEN. Sin embargo, durante las pruebas se encontró que todos los escenarios evaluados retornan consistentemente:
403 Authentication parameters missing
Para descartar errores propios, se realizaron pruebas exhaustivas:

- Consumo directo desde el backend FastAPI
- Solicitudes desde Swagger/OpenAPI
- Pruebas con curl
- Validación de parámetros según documentación oficial
- Verificación de headers HTTP
- Comparación entre entorno local y despliegue en Render
- Pruebas desde el dashboard consumiendo la API desplegada

Se concluyó que la integración sí se comunica correctamente con el servicio externo, pero al parecer existe un requisito de autenticación adicional que no está documentado o que requiere una configuración específica del proveedor.
Mientras tanto, la solución funciona con un manejo controlado de errores, a nivel de API y dashboard. Se encuentra lista para conectarse en cuanto se cuente con el mecanismo de autenticación correcto.

## Decisiones de diseño

- FastAPI por su simplicidad, rendimiento y documentación automática con OpenAPI.
- API Key para proteger los endpoints de accesos no autorizados.
- cen_client.py para aislar la lógica de integración con el CEN y facilitar el mantenimiento.
- Manejo controlado de errores para que fallas externas no afecten la disponibilidad de la API.
- Streamlit para un dashboard accesible sin necesidad de conocimientos técnicos.


## Dashboard
### Vista principal
![Dashboard Principal](docs/dashboard-1.png)
### Consulta de información
![Dashboard Consulta](docs/dashboard-2.png)

## Tecnologías utilizadas:
- Python
- FastAPI
- Streamlit
- HTTPX
- Python
- Dotenv
- Uvicorn
- Git
- GitHub
- Render
- Streamlit Cloud