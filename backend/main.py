from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware

from auth import verify_api_key
from cen_client import get_costo_marginal_cen, get_medidas_cen

app = FastAPI(
    title="Grenergy API",
    description="API REST para exponer datos del proyecto Quillagua desde CEN.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/costo-marginal")
async def costo_marginal(
    fecha: str,
    key: str = Security(verify_api_key)
):
    return await get_costo_marginal_cen(fecha)


@app.get("/medidas")
async def medidas(
    fecha_inicio: str,
    fecha_fin: str,
    key: str = Security(verify_api_key)
):
    return await get_medidas_cen(
        fecha_inicio,
        fecha_fin,
    )