import os
from dotenv import load_dotenv

load_dotenv()

MY_API_KEY = os.getenv("MY_API_KEY")
CEN_API_KEY_SIPUB = os.getenv("CEN_API_KEY_SIPUB")
CEN_API_KEY_MEDIDAS = os.getenv("CEN_API_KEY_MEDIDAS")

CEN_COSTO_MARGINAL_URL = "https://sipub.api.coordinador.cl/costo-marginal-online/v4/findByDate"
CEN_MEDIDAS_URL = "https://medidas.api.coordinador.cl/medidas-v2/measurement"

BARRA_QUILLAGUA = "FRONTERA______220"
MEASURE_POINT_ID_QUILLAGUA = "FRONTERA_220_J7-J8_QUI"