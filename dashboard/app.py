import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"
API_KEY = "clave-secreta-grenergy-2024"

st.set_page_config(
    page_title="Grenergy Dashboard",
    layout="wide"
)

st.title("⚡ Grenergy - Proyecto Quillagua")
st.caption("Dashboard de consulta de datos energéticos desde API REST propia.")

fecha = st.date_input("Fecha")

if st.button("Consultar costo marginal"):
    try:
        response = requests.get(
            f"{API_URL}/costo-marginal",
            params={"fecha": str(fecha)},
            headers={"X-API-Key": API_KEY},
            timeout=20
        )

        data = response.json()

        st.subheader("Resultado de la consulta")

        if data.get("status") == 403:
            st.warning("No fue posible obtener datos reales desde el Coordinador Eléctrico Nacional.")
            col1, col2, col3 = st.columns(3)

            col1.metric("Fuente", data.get("source", "CEN"))
            col2.metric("Estado", data.get("status", "N/A"))
            col3.metric("Proyecto", "Quillagua")

            st.info(data.get("message"))
            st.code(data.get("error"), language="text")

        else:
            st.success("Datos obtenidos correctamente.")
            st.json(data)

    except Exception as e:
        st.error("Error al consultar la API.")
        st.exception(e)

        st.divider()

st.header("⚙️ Medidas / Generación")

fecha_inicio = st.date_input(
    "Fecha inicio",
    key="fecha_inicio"
)

fecha_fin = st.date_input(
    "Fecha fin",
    key="fecha_fin"
)

if st.button("Consultar medidas"):

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
                "No fue posible obtener medidas reales desde el Coordinador Eléctrico Nacional."
            )

            col1, col2, col3 = st.columns(3)

            col1.metric("Fuente", data.get("source", "CEN"))
            col2.metric("Estado", data.get("status", "N/A"))
            col3.metric("Proyecto", "Quillagua")

            st.info(data.get("message"))
            st.code(data.get("error"), language="text")

        else:

            st.success("Datos obtenidos correctamente.")
            st.json(data)

    except Exception as e:

        st.error("Error al consultar medidas.")
        st.exception(e)