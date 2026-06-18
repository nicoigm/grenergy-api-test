import httpx
from config import (
    CEN_API_KEY_SIPUB,
    CEN_API_KEY_MEDIDAS,
    CEN_COSTO_MARGINAL_URL,
    CEN_MEDIDAS_URL,
    BARRA_QUILLAGUA,
    MEASURE_POINT_ID_QUILLAGUA,
)


async def get_costo_marginal_cen(fecha: str):
    headers = {
        "Ocp-Apim-Subscription-Key": CEN_API_KEY_SIPUB,
        "Accept": "application/json",
    }

    params = {
    "startDate": fecha,
    "endDate": fecha,
    "bar_transf": BARRA_QUILLAGUA,
    }

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(
            CEN_COSTO_MARGINAL_URL,
            headers=headers,
            params=params,
        )

    if response.status_code != 200:
        return {
            "source": "CEN",
            "status": response.status_code,
            "error": response.text,
            "message": "No fue posible obtener datos reales desde CEN. Se mantiene respuesta controlada para diagnóstico.",
        }

    return response.json()


async def get_medidas_cen(fecha_inicio: str, fecha_fin: str):
    headers = {
        "Ocp-Apim-Subscription-Key": CEN_API_KEY_MEDIDAS,
        "Accept": "application/json",
    }

    params = {
        "measurePointId": MEASURE_POINT_ID_QUILLAGUA,
        "startDate": fecha_inicio,
        "endDate": fecha_fin,
    }

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(
            CEN_MEDIDAS_URL,
            headers=headers,
            params=params,
        )

    if response.status_code != 200:
        return {
            "source": "CEN",
            "status": response.status_code,
            "error": response.text,
            "message": "No fue posible obtener medidas reales desde CEN. Se mantiene respuesta controlada para diagnóstico.",
        }

    return response.json()