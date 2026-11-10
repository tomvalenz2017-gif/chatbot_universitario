import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Chatbot Universitario - SED", page_icon="🤖", layout="centered")

st.title("🤖 Asistente Virtual Inteligente (Soporte Universitario)")
st.markdown("Este bot utiliza un motor de reglas de producción conversacionales integrado con Streamlit.")

# --- BASE DE CONOCIMIENTO (Más de 20 reglas / Intenciones) ---
# Cada regla asocia una lista de palabras clave con una respuesta específica.
BASE_CONOCIMIENTO = [
    {
        "id": 1,
        "tags": ["hola", "buenos dias", "buenas tardes", "que tal", "hey"],
        "respuesta": "¡Hola! Bienvenido al sistema de consultas de la facultad. ¿En qué puedo ayudarte hoy?"
    },
    {
        "id": 2,
        "tags": ["chau", "adios", "hasta luego", "nos vemos", "gracias"],
        "respuesta": "¡De nada! Que tengas un excelente día. No dudes en volver si tenés más dudas."
    },
    {
        "id": 3,
        "tags": ["inscripcion", "inscribirme", "anotarme", "carreras"],
        "respuesta": "Dictamos carreras de Ingeniería en Sistemas, Licenciatura en Administración y Tecnicaturas. Las inscripciones están abiertas todo el mes."
    },
    {
        "id": 4,
        "tags": ["requisitos", "papeles", "documentacion", "titulo"],
        "respuesta": "Los requisitos de ingreso son: DNI actualizado, título secundario legalizado (o constancia de título en trámite) y 2 fotos tipo carnet."
    },
    {
        "id": 5,
        "tags": ["costos", "cuota", "aranceles", "precio", "pagar"],
        "respuesta": "Las cuotas se abonan del 1 al 10 de cada mes. Podés consultar los valores actualizados y descargar los cupones desde la sección de aranceles del campus."
    },
    {
        "id": 6,
        "tags": ["becas", "ayuda economica", "descuento"],
        "respuesta": "Contamos con becas de excelencia académica y ayuda socioeconómica. Las postulaciones se abren al inicio de cada cuatrimestre."
    },
    {
        "id": 7,
        "tags": ["fechas", "parciales", "calendario", "examenes"],
        "respuesta": "El calendario académico con las fechas de los parciales y cierres de actas está publicado en la pestaña 'Calendario' de la página web oficial."
    },
    {
        "id": 8,
        "tags": ["horarios", "cursada", "clases", "turno"],
        "respuesta": "Tenemos turnos mañana (8:00 a 12:30), tarde (14:00 a 18:00) y noche (18:30 a 22:30). Los horarios específicos dependen de tu comisión."
    },
    {
        "id": 9,
        "tags": ["ubicacion", "donde", "facultad", "direccion", "aulas"],
        "respuesta": "El edificio central está ubicado en Av. Independencia 1800. Las aulas de posgrado se encuentran en el anexo norte."
    },
    {
        "id": 10,
        "tags": ["certificado", "alumno regular", "constancia"],
        "respuesta": "El certificado de alumno regular se solicita de forma online ingresando al sistema de autogestión de estudiantes (Guaraní/Campus)."
    },
    {
        "id": 11,
        "tags": ["bedelia", "contacto", "oficina de alumnos"],
        "respuesta": "Podés comunicarte con Bedelía de lunes a viernes de 9:00 a 17:00 hs en la oficina 102 o al correo bedelia@facultad.edu.ar."
    },
    {
        "id": 12,
        "tags": ["campus virtual", "plataforma", "entrar", "login"],
        "respuesta": "Para ingresar al campus virtual debes usar tu DNI como usuario y la contraseña que recibiste por mail al inscribirte."
    },
    {
        "id": 13,
        "tags": ["clave", "contrasena", "olvide", "recuperar"],
        "respuesta": "Si olvidaste tu contraseña, podés hacer clic en '¿Olvidó su contraseña?' en la pantalla de login del campus para recibir un enlace de blanqueo."
    },
    {
        "id": 14,
        "tags": ["finales", "mesas", "inscribirme a finales"],
        "respuesta": "La inscripción a mesas de exámenes finales cierra siempre 48 horas hábiles antes de la fecha estipulada del examen."
    },
    {
        "id": 15,
        "tags": ["cambio de carrera", "pase", "pasantias"],
        "respuesta": "Los trámites de cambio de carrera se realizan únicamente durante los periodos de habilitación de pases entre los meses de diciembre y febrero."
    },
    {
        "id": 16,
        "tags": ["titulo", "egreso", "graduacion", "analitico"],
        "respuesta": "Una vez aprobada la última materia, el trámite de titulación demora aproximadamente entre 60 y 90 días hábiles en ser emitido por rectorado."
    },
    {
        "id": 17,
        "tags": ["profesores", "docentes", "mail de profesores", "contacto docente"],
        "respuesta": "Los correos electrónicos institucionales de los profesores de cada cátedra se encuentran detallados en el programa analítico de la materia."
    },
    {
        "id": 18,
        "tags": ["talleres", "cursos", "extraterriculares", "idiomas"],
        "respuesta": "Ofrecemos talleres de programación avanzada, robótica e idiomas (Inglés y Portugués) con certificación oficial para estudiantes activos."
    },
    {
        "id": 19,
        "tags": ["comedor", "buffet", "almuerzo", "cafeteria"],
        "respuesta": "El comedor universitario está abierto de 11:30 a 14:30 hs y ofrece menú estudiantil subsidiado. Queda en el patio central."
    },
    {
        "id": 20,
        "tags": ["ayuda", "que puedes hacer", "opciones", "menu"],
        "respuesta": "Puedo ayudarte con información sobre inscripciones, requisitos, costos, becas, horarios, campus virtual, certificados y mesas de examen. ¡Pregúntame lo que necesites!"
    }
]

# --- FUNCIÓN DE INFERENCIA (Motor de Reglas) ---
def motor_inferencia(texto_usuario):
    texto_usuario = texto_usuario.lower()
    
    # Evaluar regla por regla buscando coincidencias de palabras clave
    for regla in BASE_CONOCIMIENTO:
        for tag in regla["tags"]:
            if tag in texto_usuario:
                return regla["respuesta"]
                
    # Respuesta por defecto si ninguna regla se activa
    return "No logré comprender del todo tu consulta. Podés intentar reformularla o escribir 'ayuda' para ver los temas que manejo."

# --- INTERFAZ DE USUARIO EN STREAMLIT ---

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Renderizar historial previo
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capturar entrada del usuario
if prompt := st.chat_input("Escribe tu consulta..."):
    # Guardar y mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Procesar la respuesta con el motor de inferencia
    respuesta_bot = motor_inferencia(prompt)

    # Guardar y mostrar respuesta del bot
    with st.chat_message("assistant"):
        st.markdown(respuesta_bot)
    st.session_state.messages.append({"role": "assistant", "content": respuesta_bot})
