import streamlit as st

st.set_page_config(page_title="Mi Aplicación", layout="wide")


def home():
    st.title("Home")
    st.write("Bienvenido a la aplicación. Selecciona un ejercicio en el menú lateral.")


def ejercicio_1():
    st.title("Ejercicio 1")
    st.write("Contenido del Ejercicio 1.")


def ejercicio_2():
    st.title("Ejercicio 2")
    st.write("Contenido del Ejercicio 2.")


def ejercicio_3():
    st.title("Ejercicio 3")
    st.write("Contenido del Ejercicio 3.")


def ejercicio_4():
    st.title("Ejercicio 4")
    st.write("Contenido del Ejercicio 4.")


# Menú lateral de navegación
st.sidebar.title("Navegación")
opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4")
)

# Enrutamiento según la opción seleccionada
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
