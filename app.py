import streamlit as st
import pandas as pd
import numpy as np
from libreria_funciones_proyecto1 import calcular_indicadores_mantenimiento, calcular_oee
from libreria_clases_proyecto1 import EquipoMantenimiento

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
 
    st.markdown(
        """
        ### Uso de funciones desde una librería externa
        En esta sección se conecta funciones de la librería `libreria_funciones_proyecto1.py`
        con la interfaz de Streamlit. Se selecciona dos funciones del área de
        Mantenimiento, que se relacionan con la gestión de flota:
 
        - Indicadores de Mantenimiento: calcula MTBF, MTTR y disponibilidad.
        - OEE: calcula la Efectividad Global del Equipo.
        """
    )
 
    st.markdown("---")
 
    if "historico_mantenimiento" not in st.session_state:
        st.session_state.historico_mantenimiento = []
 
    # Selector
    funcion = st.selectbox(
        "Selecciona la función a ejecutar",
        (
            "Indicadores de Mantenimiento (MTBF, MTTR, Disponibilidad)",
            "OEE (Efectividad Global del Equipo)",
        ),
    )
 
    st.markdown("#### Parámetros")
 
    if funcion == "Indicadores de Mantenimiento (MTBF, MTTR, Disponibilidad)":
        col1, col2, col3 = st.columns(3)
 
        with col1:
            tiempo_operacion_h = st.number_input(
                "Tiempo de operación (horas)", min_value=0.0, step=1.0, format="%.2f"
            )
 
        with col2:
            numero_fallas = st.number_input("Número de fallas", min_value=0, step=1)
 
        with col3:
            tiempo_reparacion_total_h = st.number_input(
                "Tiempo total de reparación (horas)", min_value=0.0, step=1.0, format="%.2f"
            )
 
        if st.button("Calcular"):
            try:
                resultado = calcular_indicadores_mantenimiento(
                    tiempo_operacion_h, numero_fallas, tiempo_reparacion_total_h
                )
 
                st.write("**Resultado:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("MTBF (h)", resultado["mtbf_h"])
                m2.metric("MTTR (h)", resultado["mttr_h"])
                m3.metric("Disponibilidad", f"{resultado['disponibilidad_pct']}%")
 
                st.session_state.historico_mantenimiento.append(
                    {
                        "Función": "Indicadores de Mantenimiento",
                        "Tiempo Operación (h)": tiempo_operacion_h,
                        "N° Fallas": numero_fallas,
                        "Tiempo Reparación (h)": tiempo_reparacion_total_h,
                        "MTBF (h)": resultado["mtbf_h"],
                        "MTTR (h)": resultado["mttr_h"],
                        "Disponibilidad (%)": resultado["disponibilidad_pct"],
                    }
                )
            except ValueError as e:
                st.error(f"Error en los datos ingresados: {e}")
 
    else:
        col1, col2, col3 = st.columns(3)
 
        with col1:
            disponibilidad_pct = st.number_input(
                "Disponibilidad (%)", min_value=0.0, max_value=100.0, step=1.0, format="%.2f"
            )
 
        with col2:
            rendimiento_pct = st.number_input(
                "Rendimiento (%)", min_value=0.0, max_value=100.0, step=1.0, format="%.2f"
            )
 
        with col3:
            calidad_pct = st.number_input(
                "Calidad (%)", min_value=0.0, max_value=100.0, step=1.0, format="%.2f"
            )
 
        if st.button("Calcular"):
            try:
                resultado = calcular_oee(disponibilidad_pct, rendimiento_pct, calidad_pct)
 
                st.write("**Resultado:**")
                st.metric("OEE", f"{resultado['oee_pct']}%")
 
                st.session_state.historico_mantenimiento.append(
                    {
                        "Función": "OEE",
                        "Disponibilidad (%)": disponibilidad_pct,
                        "Rendimiento (%)": rendimiento_pct,
                        "Calidad (%)": calidad_pct,
                        "OEE (%)": resultado["oee_pct"],
                    }
                )
            except ValueError as e:
                st.error(f"Error en los datos ingresados: {e}")
 
    st.markdown("---")
 
    st.subheader("Histórico de resultados")
 
    if len(st.session_state.historico_mantenimiento) == 0:
        st.info("No se han calculado resultados.")
    else:
        df_historico = pd.DataFrame(st.session_state.historico_mantenimiento)
        st.dataframe(df_historico, use_container_width=True)


def ejercicio_4():
    st.title("Ejercicio 4")
 
    st.markdown(
        """
        ### Uso de clases desde una librería externa con CRUD
        En esta sección se conecta la clase `EquipoMantenimiento` de `libreria_clases_proyecto1.py`
        con Streamlit. Para cada equipo se calcula el MTBF, MTTR y disponibilidad a partir 
        de sus horas de operación, número de fallas y horas de reparación.
        """
    )
 
    st.markdown("---")
 
    if "equipos" not in st.session_state:
        st.session_state.equipos = []  # Lista de diccionarios
    if "siguiente_id" not in st.session_state:
        st.session_state.siguiente_id = 1
    if "mensaje_exito_4" not in st.session_state:
        st.session_state.mensaje_exito_4 = None
 
    # Mostrar el mensaje de éxito anterior
    if st.session_state.mensaje_exito_4:
        st.success(st.session_state.mensaje_exito_4)
        st.session_state.mensaje_exito_4 = None
 
    def registrar_equipo(nombre, horas_operacion, numero_fallas, horas_reparacion):
        equipo = EquipoMantenimiento(nombre, horas_operacion, numero_fallas, horas_reparacion)
        resumen = equipo.resumen()
        return {
            "id": st.session_state.siguiente_id,
            "nombre_equipo": resumen["equipo"],
            "horas_operacion": horas_operacion,
            "numero_fallas": numero_fallas,
            "horas_reparacion": horas_reparacion,
            "mtbf_h": resumen["mtbf_h"],
            "mttr_h": resumen["mttr_h"],
            "disponibilidad_pct": resumen["disponibilidad_pct"],
        }
 
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(
        ["Crear", "Leer", "Actualizar", "Eliminar"]
    )
 
    # Crear
    with tab_crear:
        st.subheader("Registrar nuevo equipo")
 
        col1, col2, col3, col4 = st.columns(4)
 
        with col1:
            nombre_c = st.text_input("Nombre del equipo", key="crear_nombre")
        with col2:
            horas_operacion_c = st.number_input(
                "Horas de operación", min_value=0.0, step=1.0, format="%.2f", key="crear_operacion"
            )
        with col3:
            numero_fallas_c = st.number_input(
                "Número de fallas", min_value=0, step=1, key="crear_fallas"
            )
        with col4:
            horas_reparacion_c = st.number_input(
                "Horas de reparación", min_value=0.0, step=1.0, format="%.2f", key="crear_reparacion"
            )
 
        if st.button("Crear equipo"):
            if nombre_c.strip() == "":
                st.error("Debes ingresar el nombre del equipo.")
            else:
                try:
                    nuevo = registrar_equipo(
                        nombre_c, horas_operacion_c, numero_fallas_c, horas_reparacion_c
                    )
                    st.session_state.equipos.append(nuevo)
                    st.session_state.siguiente_id += 1
                    st.success(f"Equipo '{nombre_c}' creado correctamente.")
                except ValueError as e:
                    st.error(f"Error en los datos ingresados: {e}")
 
    # Leer
    with tab_leer:
        st.subheader("Equipos registrados")
 
        if len(st.session_state.equipos) == 0:
            st.info("Aún no hay equipos registrados.")
        else:
            df_equipos = pd.DataFrame(st.session_state.equipos)
            st.dataframe(df_equipos, use_container_width=True)
 
    # Actualizar
    with tab_actualizar:
        st.subheader("Actualizar equipo")
 
        if len(st.session_state.equipos) == 0:
            st.info("Aún no hay equipos registrados.")
        else:
            opciones = {
                f"{e['id']} - {e['nombre_equipo']}": e["id"] for e in st.session_state.equipos
            }
            seleccion = st.selectbox("Selecciona el equipo a actualizar", list(opciones.keys()))
            id_seleccionado = opciones[seleccion]
            equipo_actual = next(e for e in st.session_state.equipos if e["id"] == id_seleccionado)
 
            col1, col2, col3, col4 = st.columns(4)
 
            with col1:
                nombre_u = st.text_input(
                    "Nombre del equipo", value=equipo_actual["nombre_equipo"], key="act_nombre"
                )
            with col2:
                horas_operacion_u = st.number_input(
                    "Horas de operación",
                    min_value=0.0,
                    step=1.0,
                    format="%.2f",
                    value=float(equipo_actual["horas_operacion"]),
                    key="act_operacion",
                )
            with col3:
                numero_fallas_u = st.number_input(
                    "Número de fallas",
                    min_value=0,
                    step=1,
                    value=int(equipo_actual["numero_fallas"]),
                    key="act_fallas",
                )
            with col4:
                horas_reparacion_u = st.number_input(
                    "Horas de reparación",
                    min_value=0.0,
                    step=1.0,
                    format="%.2f",
                    value=float(equipo_actual["horas_reparacion"]),
                    key="act_reparacion",
                )
 
            if st.button("Actualizar equipo"):
                if nombre_u.strip() == "":
                    st.error("Debes ingresar el nombre del equipo.")
                else:
                    try:
                        equipo = EquipoMantenimiento(
                            nombre_u, horas_operacion_u, numero_fallas_u, horas_reparacion_u
                        )
                        resumen = equipo.resumen()
 
                        equipo_actual["nombre_equipo"] = resumen["equipo"]
                        equipo_actual["horas_operacion"] = horas_operacion_u
                        equipo_actual["numero_fallas"] = numero_fallas_u
                        equipo_actual["horas_reparacion"] = horas_reparacion_u
                        equipo_actual["mtbf_h"] = resumen["mtbf_h"]
                        equipo_actual["mttr_h"] = resumen["mttr_h"]
                        equipo_actual["disponibilidad_pct"] = resumen["disponibilidad_pct"]
 
                        st.session_state.mensaje_exito_4 = f"Equipo '{nombre_u}' actualizado correctamente."
                        st.rerun()
                    except ValueError as e:
                        st.error(f"Error en los datos ingresados: {e}")
 
    # Eliminar
    with tab_eliminar:
        st.subheader("Eliminar equipo")
 
        if len(st.session_state.equipos) == 0:
            st.info("Aún no hay equipos registrados.")
        else:
            opciones_del = {
                f"{e['id']} - {e['nombre_equipo']}": e["id"] for e in st.session_state.equipos
            }
            seleccion_del = st.selectbox(
                "Selecciona el equipo a eliminar", list(opciones_del.keys()), key="del_select"
            )
            id_a_eliminar = opciones_del[seleccion_del]
 
            if st.button("Eliminar equipo"):
                st.session_state.equipos = [
                    e for e in st.session_state.equipos if e["id"] != id_a_eliminar
                ]
                st.session_state.mensaje_exito_4 = "Equipo eliminado correctamente."
                st.rerun()

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
