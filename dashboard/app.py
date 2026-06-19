import streamlit as st
import requests
from pathlib import Path
import base64

API_URL = "https://grenergy-api-test.onrender.com"
API_KEY = "clave-secreta-grenergy-2024"

st.set_page_config(
    page_title="Grenergy Dashboard",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFFFFF;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #1F2933;
        margin-bottom: 0px;
        text-align: center;
    }

    .subtitle {
        color: #5F6C72;
        font-size: 16px;
        margin-bottom: 28px;
        text-align: center;
    }

    .section-title {
        font-size: 26px;
        font-weight: 700;
        color: #1F2933;
        margin-top: 24px;
        margin-bottom: 10px;
        border-left: 6px solid #7DF282;
        padding-left: 12px;
    }

    div[data-testid="stMetric"] {
        background-color: #F7F8F8;
        border-left: 6px solid #7DF282;
        padding: 18px;
        border-radius: 14px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }

    .stButton > button {
        background-color: #7DF282;
        color: #111111;
        border-radius: 10px;
        border: none;
        font-weight: 700;
        padding: 0.55rem 1rem;
    }

    .stButton > button:hover {
        background-color: #F5E618;
        color: #111111;
        border: none;
    }

    .info-box {
        background-color: #F7F8F8;
        border-left: 6px solid #93A2F5;
        padding: 16px;
        border-radius: 12px;
        margin-top: 16px;
        margin-bottom: 16px;
        color: #1F2933;
    }

    .footer {
        color: #7A858B;
        font-size: 13px;
        margin-top: 40px;
        border-top: 1px solid #E5E7EB;
        padding-top: 16px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------------
# Logo
# -----------------------------------------

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "grenergy_logo.png"

if LOGO_PATH.exists():
    logo_base64 = base64.b64encode(LOGO_PATH.read_bytes()).decode()

    st.markdown(
        f"""
        <div style="display:flex; justify-content:center; align-items:center;">
            <img src="data:image/png;base64,{logo_base64}" width="380">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("Logo no disponible en el entorno de despliegue.")

st.markdown(
    """
    <div style="text-align:center;">
        <p class="main-title">🌵⚡ Proyecto Quillagua ⚡🌵</p>
        <p class="subtitle">
            Consulta información de Costo Marginal y Medidas asociadas al proyecto Quillagua
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-box">
    Panel de consulta para información asociada al proyecto Quillagua.
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------------------
# COSTO MARGINAL
# -----------------------------------------

st.markdown(
    '<p class="section-title">Costo Marginal</p>',
    unsafe_allow_html=True
)

fecha = st.date_input(
    "Fecha",
    key="fecha_costo_marginal"
)

consultar_costo = st.button(
    "Consultar",
    key="btn_consultar_costo",
    use_container_width=True
)

if consultar_costo:

    try:

        response = requests.get(
            f"{API_URL}/costo-marginal",
            params={
                "fecha": str(fecha)
            },
            headers={
                "X-API-Key": API_KEY
            },
            timeout=20
        )

        data = response.json()

        st.subheader("Resultado de la consulta")

        if data.get("status") == 403:

            st.warning(
                "No fue posible obtener datos reales desde el Coordinador Eléctrico Nacional (CEN)."
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Fuente",
                data.get("source", "CEN")
            )

            col2.metric(
                "Estado",
                data.get("status", "N/A")
            )

            col3.metric(
                "Proyecto",
                "Quillagua"
            )

            st.info(data.get("message"))

            st.code(
                data.get("error"),
                language="text"
            )

        else:

            st.success(
                "Datos obtenidos correctamente."
            )

            st.json(data)

    except Exception as e:

        st.error(
            "Error al consultar la API."
        )

        st.exception(e)

st.divider()

# -----------------------------------------
# MEDIDAS / GENERACIÓN
# -----------------------------------------

st.markdown(
    '<p class="section-title">Medidas / Generación</p>',
    unsafe_allow_html=True
)

col_inicio, col_fin = st.columns(2)

with col_inicio:
    fecha_inicio = st.date_input(
        "Fecha inicio",
        key="fecha_inicio"
    )

with col_fin:
    fecha_fin = st.date_input(
        "Fecha fin",
        key="fecha_fin"
    )

consultar_medidas = st.button(
    "Consultar",
    key="btn_consultar_medidas",
    use_container_width=True
)

if consultar_medidas:

    try:

        response = requests.get(
            f"{API_URL}/medidas",
            params={
                "fecha_inicio": str(fecha_inicio),
                "fecha_fin": str(fecha_fin)
            },
            headers={
                "X-API-Key": API_KEY
            },
            timeout=20
        )

        data = response.json()

        st.subheader("Resultado medidas")

        if data.get("status") == 403:

            st.warning(
                "No fue posible obtener medidas reales desde el Coordinador Eléctrico Nacional (CEN)."
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Fuente",
                data.get("source", "CEN")
            )

            col2.metric(
                "Estado",
                data.get("status", "N/A")
            )

            col3.metric(
                "Proyecto",
                "Quillagua"
            )

            st.info(
                data.get("message")
            )

            st.code(
                data.get("error"),
                language="text"
            )

        else:

            st.success(
                "Datos obtenidos correctamente."
            )

            st.json(data)

    except Exception as e:

        st.error(
            "Error al consultar medidas."
        )

        st.exception(e)

st.markdown(
    """
    <div class="footer">
        <strong>Prueba Técnica Grenergy</strong><br>
        Proyecto Quillagua
    </div>
    """,
    unsafe_allow_html=True
)