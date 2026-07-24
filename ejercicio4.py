import streamlit as st
import pandas as pd
from libreria_clases_proyecto1 import Empleado

# Inicializar lista de empleados en sesión
if "empleados" not in st.session_state:
    st.session_state.empleados = []

# Descripción
st.markdown("### Ejercicio 4 – Uso de clases desde una librería externa con CRUD")
st.markdown("""
Este módulo permite administrar empleados usando la clase **Empleado**,
con operaciones CRUD: Crear, Leer, Actualizar y Eliminar.
""")

# Tabs para CRUD
tab1, tab2, tab3, tab4 = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])

# -------------------
# Crear
# -------------------
with tab1:
    st.subheader("Crear empleado")
    nombre = st.text_input("Nombre")
    salario_base = st.number_input("Salario base", min_value=0.0, step=100.0)
    porcentaje_bono = st.number_input("Porcentaje bono (%)", min_value=0.0, step=1.0)
    porcentaje_descuento = st.number_input("Porcentaje descuento (%)", min_value=0.0, step=1.0)

    if st.button("Agregar empleado"):
        if nombre and salario_base > 0:
            empleado = Empleado(nombre, salario_base, porcentaje_bono, porcentaje_descuento)
            st.session_state.empleados.append(empleado)
            st.success(f"Empleado {nombre} agregado correctamente ✅")
        else:
            st.error("Por favor ingresa un nombre y salario válido.")

# -------------------
# Leer
# -------------------
with tab2:
    st.subheader("Lista de empleados")
    if st.session_state.empleados:
        data = [emp.resumen() for emp in st.session_state.empleados]
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.info("No hay empleados registrados.")

# -------------------
# Actualizar
# -------------------
with tab3:
    st.subheader("Actualizar empleado")
    if st.session_state.empleados:
        opciones = [emp.nombre for emp in st.session_state.empleados]
        seleccionado = st.selectbox("Selecciona empleado", opciones)

        empleado = next(emp for emp in st.session_state.empleados if emp.nombre == seleccionado)

        nuevo_salario = st.number_input("Nuevo salario base", value=empleado.salario_base, step=100.0)
        nuevo_bono = st.number_input("Nuevo porcentaje bono (%)", value=empleado.porcentaje_bono, step=1.0)
        nuevo_descuento = st.number_input("Nuevo porcentaje descuento (%)", value=empleado.porcentaje_descuento, step=1.0)

        if st.button("Actualizar empleado"):
            empleado.salario_base = nuevo_salario
            empleado.porcentaje_bono = nuevo_bono
            empleado.porcentaje_descuento = nuevo_descuento
            st.success(f"Empleado {empleado.nombre} actualizado correctamente ✨")
    else:
        st.info("No hay empleados para actualizar.")

# -------------------
# Eliminar
# -------------------
with tab4:
    st.subheader("Eliminar empleado")
    if st.session_state.empleados:
        opciones = [emp.nombre for emp in st.session_state.empleados]
        seleccionado = st.selectbox("Selecciona empleado a eliminar", opciones)

        if st.button("Eliminar empleado"):
            st.session_state.empleados = [emp for emp in st.session_state.empleados if emp.nombre != seleccionado]
            st.success(f"Empleado {seleccionado} eliminado correctamente 🗑️")
    else:
        st.info("No hay empleados para eliminar.")
