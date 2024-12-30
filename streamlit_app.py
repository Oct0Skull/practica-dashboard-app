import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# configuración de la página
st.set_page_config(
    page_title = "Dashboard",
    page_icon = ":bar_chart:",
    layout = "wide"
)


# Titulo principal
st.title(":bar_chart: Data Vizualization Dashboard")
st.markdown("### explorando diferentes bibliotecas de vizualización en python")


# 1 Introducción (expander: flechita que expande lo que está dentro)
with st.expander(":memo: Introducción", expanded=True):
    st.markdown("""
    Esta aplicación muestra el uso de distintas bibliotecas de visualización en python:
    **Matplotlib**: base para visualización
    **Seaborn**: Visualización estadística de alto nivel
    **Plotly**: Gráficos interactivos
    **Streamlit**: Framework para aplicaciones de datos
    """)


    # 3 Visualizaciones con Matplotlib
    st.header(":art: Visualizaciones con Matplotlib")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Gráfico de dispersión")
        with col2:
            st.subheader("Gráfico de barras")





try:
    modapop_df = pd.read_excel("data/moda_pop.xlsx")
    paismil_df = pd.read_excel("data/pais_mil.xlsx")
    st.success(":heavy_check_mark: Datos cargados con éxito")
except Exception as e:
    st.error(f":x: Error al cargar los datos {str(e)}")
    st.error("Por favor verifique la existencia de los archivos en la carpeta :file_folder:'data' y que tengan el formato correcto.")

