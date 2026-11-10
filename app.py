import streamlit as st

st.title("🤖 Mi Chatbot Inteligente (Soporte Universitario)")

# Inicializar el historial del chat en la memoria de sesión
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar los mensajes anteriores en la pantalla
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Cuadro de texto para que el usuario escriba abajo
if prompt := st.chat_input("Escribe tu consulta aquí..."):
    # Agregar el mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- MOTOR DE RESPUESTAS (Tus "reglas" o Intents) ---
    respuesta = "No estoy seguro de entender tu consulta. ¿Podrías reformularla?"
    
    texto_usuario = prompt.lower()
    
    if "hola" in texto_usuario or "buenos días" in texto_usuario:
        respuesta = "¡Hola! ¿En qué puedo ayudarte hoy con tus trámites de la facultad?"
    elif "inscripción" in texto_usuario or "carreras" in texto_usuario:
        respuesta = "Dictamos carreras de Ingeniería, Licenciatura y Tecnicaturas. ¿Sobre cuál te gustaría información?"
    elif "requisitos" in texto_usuario or "papeles" in texto_usuario:
        respuesta = "Los requisitos son: DNI, título secundario legalizado y 2 fotos 4x4."
    elif "costos" in texto_usuario or "cuota" in texto_usuario:
        respuesta = "Las cuotas se actualizan a principios de mes. Podes consultar los valores en la sección aranceles del campus."
    # ... Aquí puedes seguir agregando más reglas/condiciones para cumplir con las 20 intenciones solicitadas ...

    # Mostrar la respuesta del bot
    with st.chat_message("assistant"):
        st.markdown(respuesta)
    
    # Guardar la respuesta en el historial
    st.session_state.messages.append({"role": "assistant", "content": respuesta})