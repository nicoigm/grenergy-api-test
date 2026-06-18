# Prueba Técnica – Grenergy

## Descripción

Este proyecto fue desarrollado como parte de una prueba técnica para Grenergy.

El objetivo consiste en exponer información relacionada con el proyecto Quillagua mediante una API REST y visualizar los resultados a través de un dashboard web.

La solución considera:

* API REST desarrollada con FastAPI.
* Autenticación mediante API Key.
* Configuración mediante variables de entorno.
* Integración con servicios del Coordinador Eléctrico Nacional (CEN).
* Dashboard desarrollado con Streamlit.
* Manejo de errores y respuestas controladas.
* Control de versiones mediante Git y GitHub.

---

## Arquitectura de la Solución

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

---

## Estructura del Proyecto

```text
grenergy-api-test
│
├── backend
│   ├── main.py
│   ├── auth.py
│   ├── config.py
│   ├── cen_client.py
│   ├── requirements.txt
│   └── .env
│
├── dashboard
│   └── app.py
│
└── README.md
```

---

## Endpoints Implementados

### Estado de Salud de la API

```http
GET /health
```

Respuesta:

```json
{
  "status": "ok"
}
```

---

### Costo Marginal

```http
GET /costo-marginal
```

Parámetros:

| Parámetro | Tipo   | Descripción       |
| --------- | ------ | ----------------- |
| fecha     | string | Fecha de consulta |

Ejemplo:

```http
GET /costo-marginal?fecha=2024-01-15
```

---

### Medidas / Generación

```http
GET /medidas
```

Parámetros:

| Parámetro    | Tipo   | Descripción   |
| ------------ | ------ | ------------- |
| fecha_inicio | string | Fecha inicial |
| fecha_fin    | string | Fecha final   |

Ejemplo:

```http
GET /medidas?fecha_inicio=2024-01-15&fecha_fin=2024-01-16
```

---

## Autenticación

Los endpoints de negocio se encuentran protegidos mediante API Key.

Header requerido:

```http
X-API-Key: <api-key>
```

---

## Instalación

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Variables de Entorno

Crear archivo `.env` dentro de la carpeta backend:

```env
MY_API_KEY=tu-api-key

CEN_API_KEY_SIPUB=tu-api-key-cen
CEN_API_KEY_MEDIDAS=tu-api-key-cen
```

---

## Ejecución del Backend

Desde la carpeta backend:

```bash
uvicorn main:app --reload
```

Documentación Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Ejecución del Dashboard

Desde la raíz del proyecto:

```bash
streamlit run dashboard/app.py
```

Dashboard disponible en:

```text
http://localhost:8501
```

---

## Manejo de Errores

La aplicación implementa manejo controlado de errores provenientes de servicios externos.

Cuando la integración con el Coordinador Eléctrico Nacional no responde correctamente, la API devuelve respuestas diagnósticas controladas, evitando fallas en el backend y en el dashboard.

Ejemplo:

```json
{
  "source": "CEN",
  "status": 403,
  "error": "Authentication parameters missing"
}
```

---

## Observaciones

La integración con los servicios del Coordinador Eléctrico Nacional fue implementada y validada a nivel de consumo HTTP, autenticación y control de errores.

Durante las pruebas realizadas, los endpoints externos respondieron con un error de autenticación:

```text
403 Authentication parameters missing
```

Por este motivo se implementó una estrategia de manejo de errores para asegurar la continuidad operacional de la API y del dashboard, manteniendo trazabilidad del problema y permitiendo futuras correcciones una vez que se disponga del mecanismo de autenticación correcto.

---

## Tecnologías Utilizadas

* Python
* FastAPI
* Streamlit
* HTTPX
* Python Dotenv
* Git
* GitHub
