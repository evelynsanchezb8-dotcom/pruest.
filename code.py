import streamlit as st
import pandas as pd

# -------------------------
# Configuración de la página
# -------------------------
st.set_page_config(
    page_title="Guía de Pruebas Estadísticas",
    page_icon="📊",
    layout="centered"
)

# -----------------------------------
# Inicialización del estado de sesión
# -----------------------------------
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answers" not in st.session_state:
    st.session_state.answers = []
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False

# ---------------------
# Banco de preguntas
# ---------------------
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
            "Relacionados (mismas personas en dos momentos)",
            "No aplica"
        ],
        "correct": 0,
        "explanation": "La independencia o relación cambia totalmente la prueba a usar."
    },
    {
        "question": "4. Para grupos independientes, ¿tus datos cumplen normalidad?",
        "options": [
            "Sí, normales o muestra grande",
            "No, claramente no normales",
            "Prefiero no paramétricos"
        ],
        "correct": 0,
        "explanation": "La normalidad define si usas pruebas paramétricas o no paramétricas."
    },
    {
        "question": "5. Si tienes 3+ grupos independientes, ¿tus datos son normales?",
        "options": ["Sí", "No", "Solo tengo 2 grupos"],
        "correct": 0,
        "explanation": "Normalidad decide entre ANOVA y Kruskal-Wallis."
    },
    {
        "question": "6. Si analizas relaciones, ¿qué tipo de variables tienes?",
        "options": [
            "Ambas continuas",
            "Ambas categóricas",
            "Una continua y otra categórica"
        ],
        "correct": 0,
        "explanation": "Variables continuas → correlación; categóricas → chi-cuadrada."
    },
    {
        "question": "7. Para variables continuas, ¿los datos son normales?",
        "options": ["Sí", "No", "No estoy seguro"],
        "correct": 0,
        "explanation": "Normalidad determina Pearson vs Spearman."
    }
]

# ---------------------
# Función para mostrar preguntas
# ---------------------
def display_question(q_index):
    q = questions[q_index]
    st.write(f"### {q['question']}")
    selected = st.radio(
        "Selecciona una opción:",
        q["options"],
        key=f"question_{q_index}"  # evita colisiones entre preguntas
    )
    return selected

# ---------------------
# Lógica principal del quiz
# ---------------------
if not st.session_state.quiz_completed:

    q_index = st.session_state.current_question

    selected_option = display_question(q_index)

    if st.button("Siguiente"):
        # Guardar respuesta
        st.session_state.answers.append(selected_option)

        # Verificar si es correcta
        correct_answer = questions[q_index]["options"][questions[q_index]["correct"]]
        if selected_option == correct_answer:
            st.session_state.score += 1

        # Avanzar a la siguiente pregunta
        st.session_state.current_question += 1

        # Revisar si ya se terminó
        if st.session_state.current_question >= len(questions):
            st.session_state.quiz_completed = True

        st.rerun()

else:
    # ---------------------
    # Pantalla de resultados
    # ---------------------
    st.success("🎉 ¡Has completado el cuestionario!")
    st.write(f"### Tu puntaje final: **{st.session_state.score} / {len(questions)}**")

    st.write("### Tus respuestas:")
    df = pd.DataFrame({
        "Pregunta": [q["question"] for q in questions],
        "Tu respuesta": st.session_state.answers,
        "Respuesta correcta": [q["options"][q["correct"]] for q in questions]
    })

    st.table(df)

    if st.button("Reiniciar"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answers = []
        st.session_state.quiz_completed = False
        st.rerun()


