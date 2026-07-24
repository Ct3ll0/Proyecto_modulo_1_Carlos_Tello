import streamlit as st
import pandas as pd

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
        """
        Breve descripción del proyecto: esta aplicación contiene 4 secciones donde se aplican conceptos fundamentales de estructura de datos,
        control de flujo, funciones, programación funcional y programación orientada a objetos
        """
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
        En esta sección se registran movimientos financieros (ingresos y gastos)
        y se muestran en una lista. Finalmente, se calcula y se muestra el total de ingresos, el total de gastos,
        el saldo final y se indica si el flujo de caja está a favor o en contra.
        """
    )
 
    st.markdown("---")
 
    # Inicializar lista de movimientos
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []
 
    # Widgets
    col1, col2, col3 = st.columns(3)
 
    with col1:
        concepto = st.text_input("Concepto")
 
    with col2:
        tipo = st.selectbox("Tipo de movimiento", ("Ingreso", "Gasto"))
 
    with col3:
        valor = st.number_input("Valor", min_value=0.0, step=0.01, format="%.2f")
 
    if st.button("Agregar movimiento"):
        if concepto.strip() == "":
            st.error("Debes ingresar un concepto")
        elif valor <= 0:
            st.error("El valor debe ser mayor a 0.")
        else:
            st.session_state.movimientos.append(
                {"Concepto": concepto, "Tipo": tipo, "Valor": valor}
            )
            st.success(f"Movimiento '{concepto}' agregado correctamente.")
 
    st.markdown("---")
 
    # Tabla de movimientos
    st.subheader("Movimientos registrados")
 
    if len(st.session_state.movimientos) == 0:
        st.info("No se han registrado movimientos.")
    else:
        df = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df, use_container_width=True)
 
        # Cálculo de totales
        total_ingresos = df.loc[df["Tipo"] == "Ingreso", "Valor"].sum()
        total_gastos = df.loc[df["Tipo"] == "Gasto", "Valor"].sum()
        saldo_final = total_ingresos - total_gastos
 
        st.markdown("---")
        st.subheader("Flujo de caja")
 
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Ingresos", f"S/ {total_ingresos:.2f}")
        m2.metric("Total Gastos", f"S/ {total_gastos:.2f}")
        m3.metric("Saldo Final", f"S/ {saldo_final:.2f}")
 
        if saldo_final >= 0:
            st.success(f"El flujo de caja está **a favor** con S/ {saldo_final:.2f}")
        else:
            st.error(f"El flujo de caja está **en contra** con S/ {saldo_final:.2f}")


def ejercicio_2():
    st.title("Ejercicio 2")
 
    st.markdown(
        """
        ### Registro con NumPy, arrays y DataFrame
        En esta sección se registran productos en arreglos de NumPy.
        Se calcula el total y todos los registros se muestran en una tabla con Pandas.
        """
    )
 
    st.markdown("---")
 
    # Inicializar arrays
    if "np_nombres" not in st.session_state:
        st.session_state.np_nombres = np.array([], dtype=str)
        st.session_state.np_categorias = np.array([], dtype=str)
        st.session_state.np_precios = np.array([], dtype=float)
        st.session_state.np_cantidades = np.array([], dtype=int)
        st.session_state.np_totales = np.array([], dtype=float)
 
    # Formulario
    col1, col2, col3, col4 = st.columns(4)
 
    with col1:
        nombre = st.text_input("Nombre del producto")
 
    with col2:
        categoria = st.selectbox(
            "Categoría",
            ("Ropa", "Electrónico", "Alimento", "Hogar", "Deporte", "Higiene", "Mascotas", "Otros"),
        )
 
    with col3:
        precio = st.number_input("Precio", min_value=0.0, step=0.01, format="%.2f")
 
    with col4:
        cantidad = st.number_input("Cantidad", min_value=0, step=1)
 
    if st.button("Agregar registro"):
        if nombre.strip() == "":
            st.error("Debes ingresar el nombre del producto.")
        elif precio <= 0:
            st.error("El precio debe ser mayor a 0.")
        elif cantidad <= 0:
            st.error("La cantidad debe ser mayor a 0.")
        else:
            total = precio * cantidad
 
            # Agregar los nuevos valores
            st.session_state.np_nombres = np.append(st.session_state.np_nombres, nombre)
            st.session_state.np_categorias = np.append(st.session_state.np_categorias, categoria)
            st.session_state.np_precios = np.append(st.session_state.np_precios, precio)
            st.session_state.np_cantidades = np.append(st.session_state.np_cantidades, cantidad)
            st.session_state.np_totales = np.append(st.session_state.np_totales, total)
 
            st.success(f"Producto '{nombre}' agregado correctamente.")
 
    st.markdown("---")
 
    # Convertir los arrays en DataFrame
    st.subheader("Registros actualizados")
 
    if len(st.session_state.np_nombres) == 0:
        st.info("No se han registrado productos.")
    else:
        df = pd.DataFrame(
            {
                "Producto": st.session_state.np_nombres,
                "Categoría": st.session_state.np_categorias,
                "Precio": st.session_state.np_precios,
                "Cantidad": st.session_state.np_cantidades,
                "Total": st.session_state.np_totales,
            }
        )
        st.dataframe(df, use_container_width=True)


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
