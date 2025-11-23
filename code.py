import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Guía de Pruebas Estadísticas",
    page_icon="📊",
    layout="centered"
)

# Inicializar estado de la sesión
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answers" not in st.session_state:
    st.session_state.answers = []
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False

# Datos del cuestionario
questions = [
    {
        "question": "1. ¿Qué tipo de objetivo principal tiene tu análisis?",
        "options": [
            "Comparar grupos entre sí",
            "Ver relaciones entre variables",
            "Predecir una variable basándome en otra",
            "Analizar frecuencias o proporciones"
        ],
        "correct": 0,
        "explanation": "Identificar si quieres comparar grupos es el primer paso fundamental."
    },
    {
        "question": "2. ¿Cuántos grupos quieres comparar?",
        "options": ["2 grupos", "3 o más grupos", "No estoy comparando grupos"],
        "correct": 0,
        "explanation": "El número de grupos determina el tipo de prueba estadística."
    },
    {
        "question": "3. ¿Los grupos que comparas son independientes o relacionados?",
        "options": [
            "Independientes (grupos diferentes)",
            "Relacionados (mismas persona

