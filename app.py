import streamlit as st

st.set_page_config(page_title="Proyecto 1 DMC", layout="wide")


def home():
    col1, col2 = st.columns([1, 3],vertical_alignment="center")
 
    with col1:
        st.image("logodmc.png", width=150)
        pass
 
    with col2:
        st.title("Proyecto 1 - Python for Analytics")
        st.subheader("Módulo 1 - Python Fundamentals")
        st.write("**Año:** 2026")
 
    st.markdown("---")
   
    st.subheader("Información del estudiante")
    col_a, col_b = st.columns(2)
 
    with col_a:
        st.write("**Nombre completo:** Carlos Andres Tello Torrejon")
        st.write("**Edad:** 31 años")
        st.write("**Profesión:** Ingeniero mecánico")
 
    with col_b:
        st.write("**Correo:** tello.carlos@pucp.pe")
        st.write("**Ciudad:** Lima, Perú")
        
    st.markdown("---")
 
    st.subheader("Descripción del proyecto")
    st.write(
        "Breve descripción del proyecto: esta aplicación contiene 4 secciones donde se aplican conceptos fundamentales de estructura de datos, control de flujo, funciones, programación funcional y programación orientada a objetos "
    )
 
    st.markdown("---")
 
    st.subheader("Tecnologías utilizadas")
    st.markdown(
        """
        - Python
        - Streamlit
        - GitHub
        - Librerías: Pandas, Numpy
        - Programación orientada a objetos
        """
    )

def ejercicio_1():
    st.title("Ejercicio 1")
 
    st.markdown(
        """
        ### Flujo de caja con listas
        En este ejercicio se registran movimientos financieros (**ingresos** y **gastos**)
        en una lista. Al final se calcula el total de ingresos, el total de gastos,
        el saldo final y si el flujo de caja está **a favor** o **en contra**.
        """
    )
 
    st.markdown("---")
 
    # Inicializar la lista de movimientos en el estado de la sesión
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []
 
    # Widgets para ingresar un nuevo movimiento
    col1, col2, col3 = st.columns(3)
 
    with col1:
        concepto = st.text_input("Concepto")
 
    with col2:
        tipo = st.selectbox("Tipo de movimiento", ("Ingreso", "Gasto"))
 
    with col3:
        valor = st.number_input("Valor", min_value=0.0, step=0.01, format="%.2f")
 
    if st.button("Agregar movimiento"):
        if concepto.strip() == "":
            st.error("Debes ingresar un concepto antes de agregar el movimiento.")
        elif valor <= 0:
            st.error("El valor debe ser mayor a 0.")
        else:
            st.session_state.movimientos.append(
                {"Concepto": concepto, "Tipo": tipo, "Valor": valor}
            )
            st.success(f"Movimiento '{concepto}' agregado correctamente.")
 
    st.markdown("---")
 
    # Mostrar la tabla de movimientos
    st.subheader("Movimientos registrados")
 
    if len(st.session_state.movimientos) == 0:
        st.info("Aún no se han registrado movimientos.")
    else:
        df = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df, use_container_width=True)
 
        # Cálculo de totales
        total_ingresos = df.loc[df["Tipo"] == "Ingreso", "Valor"].sum()
        total_gastos = df.loc[df["Tipo"] == "Gasto", "Valor"].sum()
        saldo_final = total_ingresos - total_gastos
 
        st.markdown("---")
        st.subheader("Resultado del flujo de caja")
 
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Ingresos", f"S/ {total_ingresos:.2f}")
        m2.metric("Total Gastos", f"S/ {total_gastos:.2f}")
        m3.metric("Saldo Final", f"S/ {saldo_final:.2f}")
 
        if saldo_final >= 0:
            st.success(f"El flujo de caja está A FAVOR con S/ {saldo_final:.2f}")
        else:
            st.error(f"El flujo de caja está EN CONTRA con S/ {saldo_final:.2f}")


def ejercicio_2():
    st.title("Ejercicio 2")
    st.write("Contenido del Ejercicio 2.")


def ejercicio_3():
    st.title("Ejercicio 3")
    st.write("Contenido del Ejercicio 3.")


def ejercicio_4():
    st.title("Ejercicio 4")
    st.write("Contenido del Ejercicio 4.")


# Menú lateral
st.sidebar.title("Menú")
opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4")
)

# Enrutamiento
if opcion == "Home":
    home()
elif opcion == "Ejercicio 1":
    ejercicio_1()
elif opcion == "Ejercicio 2":
    ejercicio_2()
elif opcion == "Ejercicio 3":
    ejercicio_3()
elif opcion == "Ejercicio 4":
    ejercicio_4()
