import streamlit as st
from agente import crear_agente_tutor

st.set_page_config(
    page_title="Agente Tutor de IA",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Agente Tutor de Inteligencia Artificial")

st.write(
    "Escribe un tema, selecciona tu nivel y el agente lo explicará con un ejemplo y una pregunta."
)

nivel = st.selectbox(
    "Selecciona el nivel del estudiante",
    ["Principiante", "Intermedio", "Avanzado"],
)

tema = st.text_input(
    "Tema que deseas aprender",
    placeholder="Ejemplo: aprendizaje supervisado",
)

if st.button("Explicar tema", type="primary"):
    if not tema.strip():
        st.warning("Escribe un tema.")
    else:
        mensaje = f"""
Tema: {tema}

Nivel del estudiante: {nivel}

La respuesta debe contener:

1. Una explicación sencilla.
2. Un ejemplo práctico.
3. Una analogía.
4. Una pregunta de evaluación.
"""

        with st.spinner("Generando respuesta..."):

            try:
                agente = crear_agente_tutor()

                respuesta = agente.run(mensaje)

                st.subheader("Respuesta")

                st.markdown(respuesta.content)

            except Exception as e:

                st.error(f"No fue posible conectar con LM Studio.\n\n{e}")

st.divider()

st.caption("Proyecto educativo con Python, Agno, Streamlit y LM Studio.")