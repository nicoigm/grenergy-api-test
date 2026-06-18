import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

MY_API_KEY = os.getenv("MY_API_KEY")
CEN_API_KEY_SIPUB = os.getenv("CEN_API_KEY_SIPUB")
CEN_API_KEY_MEDIDAS = os.getenv("CEN_API_KEY_MEDIDAS")

CEN_COSTO_MARGINAL_URL = "https://sipub.api.coordinador.cl:443/costo-marginal-online/v4/findByDate"
CEN_MEDIDAS_URL = "https://medidas.api.coordinador.cl:443/medidas-v2/measurement"

BARRA_QUILLAGUA = "FRONTERA______220"
MEASURE_POINT_ID_QUILLAGUA = "FRONTERA_220_J7-J8_QUI"