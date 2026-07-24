import streamlit as st
import pandas as pd
import numpy as np

# Importar librerías externas
from libreria_funciones_proyecto1 import (
    calcular_metricas_clasificacion,
    calcular_disponibilidad_sistema,
    calcular_tiempo_transferencia_archivo,
    calcular_tasa_error_transacciones,
    calcular_almacenamiento_respaldo
)
from libreria_clases_proyecto1 import Empleado

# Inicializar estados
if "empleados" not in st.session_state:
    st.session_state.empleados = []
if "historico" not in st.session_state:
    st.session_state.historico = []
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []
if "productos" not in st.session_state:
    st.session_state.productos = np.array([]).reshape(0, 5)

# Sidebar navegación
pagina = st.sidebar.selectbox(
    "Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# -------------------
# Página Home
# -------------------
if pagina == "Home":
    st.title("Trabajo Final Python Fundamentals")
    st.image("logo.png", width=150)  # Logo personal (opcional, coloca tu archivo en el repo)
    st.subheader("Estudiante: Brooke Stephannie Rojas Ortiz")
    st.subheader("Módulo 1 - Python Fundamentals")

    st.markdown("### Información General")
    st.write("**Año:** 2026")
    st.write("Este proyecto reúne ejercicios prácticos de Python aplicados con Streamlit, "
             "enfocados en fundamentos de programación, análisis de datos y desarrollo de aplicaciones interactivas.")

    st.markdown("### Tecnologías utilizadas")
    st.write("- Python")
    st.write("- NumPy")
    st.write("- Pandas")
    st.write("- Streamlit")

    st.markdown("### Ejercicios disponibles")
    st.write("1. Flujo de caja con listas")
    st.write("2. Registro con NumPy y DataFrame")
    st.write("3. Uso de funciones desde librería externa")
    st.write("4. Uso de clases desde librería externa con CRUD")

# -------------------
# Ejercicio 1 – Flujo de caja
# -------------------
elif pagina == "Ejercicio 1":
    st.title("Ejercicio 1 – Flujo de Caja con Listas")
    concepto = st.text_input("Concepto del movimiento")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=10.0)

    if st.button("Agregar movimiento"):
        if concepto and valor > 0:
            st.session_state.movimientos.append({"Concepto": concepto, "Tipo": tipo, "Valor": valor})
            st.success("Movimiento agregado correctamente ✅")
        else:
            st.error("Por favor ingresa un concepto y un valor mayor a 0.")

    if st.session_state.movimientos:
        df = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df)
        total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos
        st.metric("Total Ingresos", f"S/. {total_ingresos:,.2f}")
        st.metric("Total Gastos", f"S/. {total_gastos:,.2f}")
        st.metric("Saldo Final", f"S/. {saldo_final:,.2f}")
        if saldo_final >= 0:
            st.success("El flujo de caja está **a favor** 💹")
        else:
            st.error("El flujo de caja está **en contra** 📉")

# -------------------
# Ejercicio 2 – Registro con NumPy
# -------------------
elif pagina == "Ejercicio 2":
    st.title("Ejercicio 2 – Registro con NumPy y DataFrame")
    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Electrónica", "Ropa", "Alimentos", "Otros"])
    precio = st.number_input("Precio", min_value=0.0, step=1.0)
    cantidad = st.number_input("Cantidad", min_value=0, step=1)

    if st.button("Agregar registro"):
        if nombre and precio > 0 and cantidad > 0:
            total = precio * cantidad
            nuevo_registro = np.array([[nombre, categoria, precio, cantidad, total]])
            st.session_state.productos = np.vstack([st.session_state.productos, nuevo_registro])
            st.success("Registro agregado correctamente ✅")
        else:
            st.error("Por favor ingresa todos los datos correctamente.")

    if st.session_state.productos.shape[0] > 0:
        columnas = ["Nombre", "Categoría", "Precio", "Cantidad", "Total"]
        df = pd.DataFrame(st.session_state.productos, columns=columnas)
        st.dataframe(df)

# -------------------
# Ejercicio 3 – Funciones externas
# -------------------
elif pagina == "Ejercicio 3":
    st.title("Ejercicio 3 – Uso de funciones desde librería externa")
    funcion = st.selectbox("Selecciona la función", [
        "Calcular métricas de clasificación",
        "Calcular disponibilidad del sistema",
        "Calcular tiempo de transferencia de archivo",
        "Calcular tasa de error de transacciones",
        "Calcular almacenamiento de respaldo"
    ])
    parametros = {}
    if funcion == "Calcular métricas de clasificación":
        tp = st.number_input("TP", min_value=0, step=1)
        fp = st.number_input("FP", min_value=0, step=1)
        fn = st.number_input("FN", min_value=0, step=1)
        parametros = {"tp": tp, "fp": fp, "fn": fn}
    elif funcion == "Calcular disponibilidad del sistema":
        tiempo_total = st.number_input("Tiempo total (horas)", min_value=0.0, step=1.0)
        tiempo_caida = st.number_input("Tiempo de caída (horas)", min_value=0.0, step=1.0)
        parametros = {"tiempo_total_horas": tiempo_total, "tiempo_caida_horas": tiempo_caida}
    elif funcion == "Calcular tiempo de transferencia de archivo":
        tamano = st.number_input("Tamaño archivo (MB)", min_value=0.0, step=1.0)
        velocidad = st.number_input("Velocidad (Mbps)", min_value=0.1, step=0.1)
        parametros = {"tamano_mb": tamano, "velocidad_mbps": velocidad}
    elif funcion == "Calcular tasa de error de transacciones":
        fallidas = st.number_input("Transacciones fallidas", min_value=0, step=1)
        totales = st.number_input("Transacciones totales", min_value=1, step=1)
        parametros = {"transacciones_fallidas": fallidas, "transacciones_totales": totales}
    elif funcion == "Calcular almacenamiento de respaldo":
        usuarios = st.number_input("Número de usuarios", min_value=1, step=1)
        archivos = st.number_input("Archivos por usuario", min_value=1, step=1)
        tamano_promedio = st.number_input("Tamaño promedio archivo (MB)", min_value=0.1, step=0.1)
        factor = st.number_input("Factor respaldo", min_value=0.1, step=0.1)
        parametros = {"numero_usuarios": usuarios, "archivos_por_usuario": archivos,
                      "tamano_promedio_mb": tamano_promedio, "factor_respaldo": factor}

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
            st.write("### Resultado")
            st.write(resultado)
            registro = {"funcion": funcion, **parametros, **resultado}
            st.session_state.historico.append(registro)
        except Exception as e:
            st.error(f"Error: {e}")

    if st.session_state.historico:
        df = pd.DataFrame(st.session_state.historico)
        st.dataframe(df)

# -------------------
# Ejercicio 4 – Clases con CRUD
# -------------------
elif pagina == "Ejercicio 4":
    st.title("Ejercicio 4 – Uso de clases con CRUD")
    tab1, tab2, tab3, tab4 = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])

    # Crear
    with tab1:
        nombre = st.text_input("Nombre")
