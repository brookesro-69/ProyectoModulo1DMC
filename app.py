import streamlit as st
st.title("Proyecto Módulo 1 Fundamentals")
st.sidebar.title("Parámetros")

valor_inicial = st.number_input("Ingrese el valor inicial", value = 0)
valor_final = st.number_input("Ingrese el valor final", value = 1)

lista_numerica = list(range(valor_inicial,valor_final))
