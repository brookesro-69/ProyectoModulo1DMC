import streamlit as st
import pandas as pd

# Inicializar lista de movimientos en sesión
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

# Descripción del ejercicio
st.markdown("### Ejercicio 1 – Flujo de Caja con Listas")
st.markdown("""
Este módulo permite registrar movimientos financieros (ingresos y gastos) 
y calcular el saldo final del flujo de caja.
""")

# Widgets para ingresar datos
concepto = st.text_input("Concepto del movimiento")
tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
valor = st.number_input("Valor", min_value=0.0, step=10.0)

# Botón para agregar movimiento
if st.button("Agregar movimiento"):
    if concepto and valor > 0:
        st.session_state.movimientos.append({
            "Concepto": concepto,
            "Tipo": tipo,
            "Valor": valor
        })
        st.success("Movimiento agregado correctamente ✅")
    else:
        st.error("Por favor ingresa un concepto y un valor mayor a 0.")

# Mostrar lista de movimientos
if st.session_state.movimientos:
    df = pd.DataFrame(st.session_state.movimientos)
    st.dataframe(df)

    # Calcular totales
    total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
    total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
    saldo_final = total_ingresos - total_gastos

    # Mostrar métricas
    st.metric("Total Ingresos", f"S/. {total_ingresos:,.2f}")
    st.metric("Total Gastos", f"S/. {total_gastos:,.2f}")
    st.metric("Saldo Final", f"S/. {saldo_final:,.2f}")

    # Estado del flujo de caja
    if saldo_final >= 0:
        st.success("El flujo de caja está **a favor** 💹")
    else:
        st.error("El flujo de caja está **en contra** 📉")
