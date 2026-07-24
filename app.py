import streamlit as st

st.set_page_config(page_title="Proyecto 1 DMC", layout="wide")


def home():
    col1, col2 = st.columns([1, 3])
 
    with col1:
        # Reemplaza "logo.png" por el nombre de tu logo/imagen (debe estar en la misma carpeta)
        # st.image("logo.png", width=150)
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
 
    st.subheader("Descripción del Proyecto")
    st.write(
        "Breve descripción del proyecto: esta aplicación contiene 4 secciones donde se aplican conceptos fundamentales de estructura de datos, control de flujo, funciones, programación funcional y programación orientada a objetos "
    )
 
    st.markdown("---")
 
    st.subheader("Tecnologías Utilizadas")
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
