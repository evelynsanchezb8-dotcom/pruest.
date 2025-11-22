import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Guía de Pruebas Estadísticas",
    page_icon="📊",
    layout="centered"
)

# Inicializar estado de la sesión
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False

# Datos de las preguntas
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
        "explanation": "✅ Correcto! Identificar si quieres comparar grupos es el primer paso fundamental. Esto determina toda la ruta de análisis posterior."
    },
    {
        "question": "2. ¿Cuántos grupos quieres comparar?",
        "options": [
            "2 grupos",
            "3 o más grupos", 
            "No estoy comparando grupos"
        ],
        "correct": 0,
        "explanation": "✅ Correcto! El número de grupos (2 vs 3+) determina si usas pruebas para comparaciones binarias o múltiples."
    },
    {
        "question": "3. ¿Los grupos que comparas son independientes o relacionados?",
        "options": [
            "Independientes (grupos diferentes de personas/objetos)",
            "Relacionados (mismo grupo en diferentes momentos/condiciones)",
            "No aplica - no estoy comparando grupos"
        ],
        "correct": 0,
        "explanation": "✅ Correcto! Los grupos independientes vienen de muestras diferentes, los relacionados son las mismas unidades medidas múltiples veces."
    },
    {
        "question": "4. Para grupos independientes, ¿tus datos cumplen con normalidad?",
        "options": [
            "Sí, datos normales (o no estoy seguro pero la muestra es grande)",
            "No, datos claramente no normales",
            "Prefiero usar método no paramétrico por seguridad"
        ],
        "correct": 0,
        "explanation": "✅ Correcto! La normalidad decide entre métodos paramétricos (más potencia si se cumple) vs no paramétricos (más robustos)."
    },
    {
        "question": "5. Si tienes 3+ grupos independientes, ¿tus datos son normales?",
        "options": [
            "Sí, datos normales",
            "No, datos no normales", 
            "Solo tengo 2 grupos"
        ],
        "correct": 0,
        "explanation": "✅ Correcto! Para múltiples grupos, la normalidad determina si usas ANOVA (paramétrico) o Kruskal-Wallis (no paramétrico)."
    },
    {
        "question": "6. Si analizas relaciones, ¿qué tipo de variables tienes?",
        "options": [
            "Ambas variables son continuas (ej: edad, peso, ingresos)",
            "Ambas variables son categóricas (ej: género, preferencia)",
            "Una es continua y otra categórica"
        ],
        "correct": 0,
        "explanation": "✅ Correcto! Variables continuas requieren correlación, categóricas requieren chi-cuadrada."
    },
    {
        "question": "7. Para variables continuas, ¿los datos son normales?",
        "options": [
            "Sí, distribución normal",
            "No, distribución no
