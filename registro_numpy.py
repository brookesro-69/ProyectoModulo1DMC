import streamlit as st
import numpy as np
import pandas as pd

# Inicializar arrays en sesión
if "productos" not in st.session_state:
    st.session_state.productos = np.array([]).reshape(0, 5)  # columnas: nombre, categoría, precio, cantidad, total

# Descripción del ejercicio
st.markdown("### Ejercicio 2 – Registro con NumPy, arrays y DataFrame")
st.markdown("""
Este módulo permite registrar productos con sus atributos (nombre, categoría, precio, cantidad y total),
almacenarlos en arrays de NumPy y mostrarlos en un DataFrame actualizado.
""")

# Formulario de ingreso de datos
nombre = st.text_input("Nombre del producto")
categoria = st.selectbox("Categoría", ["Electrónica", "Ropa", "Alimentos", "Otros"])
precio = st.number_input("Precio", min_value=0.0, step=1.0)
cantidad = st.number_input("Cantidad", min_value=0, step=1)

# Botón para agregar registro
if st.button("Agregar registro"):
    if nombre and precio > 0 and cantidad > 0:
        total = precio * cantidad
        nuevo_registro = np.array([[nombre, categoria, precio, cantidad, total]])
        st.session_state.productos = np.vstack([st.session_state.productos, nuevo_registro])
        st.success("Registro agregado correctamente ✅")
    else:
        st.error("Por favor ingresa todos los datos correctamente.")

# Mostrar DataFrame actualizado
if st.session_state.productos.shape[0] > 0:
    columnas = ["Nombre", "Categoría", "Precio", "Cantidad", "Total"]
    df = pd.DataFrame(st.session_state.productos, columns=columnas)
    st.dataframe(df)
