import streamlit as st
import pandas as pd
from libreria_funciones_proyecto1 import (
    calcular_metricas_clasificacion,
    calcular_disponibilidad_sistema,
    calcular_tiempo_transferencia_archivo,
    calcular_tasa_error_transacciones,
    calcular_almacenamiento_respaldo
)

# Inicializar histórico en sesión
if "historico" not in st.session_state:
    st.session_state.historico = []

# Descripción
st.markdown("### Ejercicio 3 – Uso de funciones desde una librería externa")
st.markdown("""
Este módulo permite seleccionar una función de la librería externa, ingresar parámetros,
ejecutar el cálculo y mostrar los resultados junto con un histórico en DataFrame.
""")

# Selector de función
funcion = st.selectbox(
    "Selecciona la función a ejecutar",
    [
        "Calcular métricas de clasificación",
        "Calcular disponibilidad del sistema",
        "Calcular tiempo de transferencia de archivo",
        "Calcular tasa de error de transacciones",
        "Calcular almacenamiento de respaldo"
    ]
)

# Widgets dinámicos según la función seleccionada
parametros = {}
if funcion == "Calcular métricas de clasificación":
    tp = st.number_input("True Positives (TP)", min_value=0, step=1)
    fp = st.number_input("False Positives (FP)", min_value=0, step=1)
    fn = st.number_input("False Negatives (FN)", min_value=0, step=1)
    parametros = {"tp": tp, "fp": fp, "fn": fn}

elif funcion == "Calcular disponibilidad del sistema":
    tiempo_total = st.number_input("Tiempo total (horas)", min_value=0.0, step=1.0)
    tiempo_caida = st.number_input("Tiempo de caída (horas)", min_value=0.0, step=1.0)
    parametros = {"tiempo_total_horas": tiempo_total, "tiempo_caida_horas": tiempo_caida}

elif funcion == "Calcular tiempo de transferencia de archivo":
    tamano = st.number_input("Tamaño del archivo (MB)", min_value=0.0, step=1.0)
    velocidad = st.number_input("Velocidad (Mbps)", min_value=0.1, step=0.1)
    parametros = {"tamano_mb": tamano, "velocidad_mbps": velocidad}

elif funcion == "Calcular tasa de error de transacciones":
    fallidas = st.number_input("Transacciones fallidas", min_value=0, step=1)
    totales = st.number_input("Transacciones totales", min_value=1, step=1)
    parametros = {"transacciones_fallidas": fallidas, "transacciones_totales": totales}

elif funcion == "Calcular almacenamiento de respaldo":
    usuarios = st.number_input("Número de usuarios", min_value=1, step=1)
    archivos = st.number_input("Archivos por usuario", min_value=1, step=1)
    tamano_promedio = st.number_input("Tamaño promedio por archivo (MB)", min_value=0.1, step=0.1)
    factor = st.number_input("Factor de respaldo", min_value=0.1, step=0.1)
    parametros = {
        "numero_usuarios": usuarios,
        "archivos_por_usuario": archivos,
        "tamano_promedio_mb": tamano_promedio,
        "factor_respaldo": factor
    }

# Botón para ejecutar
if st.button("Ejecutar función"):
    try:
        if funcion == "Calcular métricas de clasificación":
            resultado = calcular_metricas_clasificacion(**parametros)
        elif funcion == "Calcular disponibilidad del sistema":
            resultado = calcular_disponibilidad_sistema(**parametros)
        elif funcion == "Calcular tiempo de transferencia de archivo":
            resultado = calcular_tiempo_transferencia_archivo(**parametros)
        elif funcion == "Calcular tasa de error de transacciones":
            resultado = calcular_tasa_error_transacciones(**parametros)
        elif funcion == "Calcular almacenamiento de respaldo":
            resultado = calcular_almacenamiento_respaldo(**parametros)

        # Mostrar resultado
        st.write("### Resultado")
        st.write(resultado)

        # Guardar en histórico
        registro = {"funcion": funcion, **parametros, **resultado}
        st.session_state.historico.append(registro)

    except Exception as e:
        st.error(f"Error: {e}")

# Mostrar histórico
if st.session_state.historico:
    df = pd.DataFrame(st.session_state.historico)
    st.dataframe(df)
