from fastapi import FastAPI, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Grenergy API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MY_API_KEY = os.getenv("MY_API_KEY")
api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(key: str = Security(api_key_header)):
    if key != MY_API_KEY:
        raise HTTPException(status_code=403, detail="API Key inválida")
    return key

CEN_KEY_SIPUB = os.getenv("CEN_API_KEY_SIPUB")
CEN_KEY_MEDIDAS = os.getenv("CEN_API_KEY_MEDIDAS")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/costo-marginal")
async def get_costo_marginal(fecha: str, key: str = Security(verify_api_key)):
    url = "https://sipub.api.coordinador.cl/costo-marginal-online/v4/findByDate"
    headers = {
        "apikey": CEN_KEY_SIPUB,
        "Accept": "application/json"
    }
    params = {
        "fecha": fecha,
        "codigoBarraStr": "FRONTERA______220"
    }
    print("HEADER ENVIADO:")
    print(headers)
    async with httpx.AsyncClient(verify=False) as client:
        r = await client.get(url, headers=headers, params=params)
        return {"status": r.status_code, "body": r.text}


@app.get("/medidas")
async def get_medidas(fecha_inicio: str, fecha_fin: str, key: str = Security(verify_api_key)):
    url = "https://medidas.api.coordinador.cl/medidas-v2/measurement"
    headers = {
        "Ocp-Apim-Subscription-Key": CEN_KEY_MEDIDAS,
        "Accept": "application/json"
    }
    params = {
        "measurePointId": "FRONTERA_220_J7-J8_QUI",
        "startDate": fecha_inicio,
        "endDate": fecha_fin
    }
    async with httpx.AsyncClient(verify=False) as client:
        r = await client.get(url, headers=headers, params=params)
        return {"status": r.status_code, "body": r.text}