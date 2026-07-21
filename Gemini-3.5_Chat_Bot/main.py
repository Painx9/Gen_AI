import os
import json

import streamlit as st
from google import genai

# Load API key safely for both local use and Streamlit Cloud secrets
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    working_dir = os.path.dirname(os.path.abspath(__file__))
    config_data = json.load(open(f"{working_dir}/config.json"))
    GEMINI_API_KEY = config_data["GEMINI_API_KEY"]

# initialize the google genai client
client = genai.Client(api_key=GEMINI_API_KEY)

# configuring streamlit page settings
st.set_page_config(
    page_title="Gemini Chat",
    page_icon="💬",
    layout="centered"
)

# initialize chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# streamlit page title
st.title("🤖 Gemini 3.5 Flash-Lite - ChatBot")

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input field for user's message
user_prompt = st.chat_input("Ask Gemini...")

if user_prompt:
    # add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Building context from chat history for Gemini
    formatted_history = []
    for msg in st.session_state.chat_history[:-1]:
        role = "user" if msg["role"] == "user" else "model"
        formatted_history.append({"role": role, "parts": [{"text": msg["content"]}]})

    try:
        # Create chat session with history and send message using gemini-3.5-flash-lite
        chat = client.chats.create(model="gemini-3.5-flash-lite", history=formatted_history)
        response = chat.send_message(user_prompt)
        assistant_response = response.text

        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

        # display Gemini's response
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    except Exception as e:
        st.error(f"An error occurred: {e}")
