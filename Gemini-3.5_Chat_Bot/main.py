import os
import json
import streamlit as st
from google import genai

# configuring streamlit page settings
st.set_page_config(
    page_title="Gemini Chat",
    page_icon="💬",
    layout="centered"
)

# streamlit page title
st.title("🤖 Gemini - ChatBot")

# Sidebar for user inputs / API key
with st.sidebar:
    st.header("Configuration")
    user_api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.markdown("[Get a Gemini API Key from Google AI Studio](https://aistudio.google.com/)")
    st.markdown("---")
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

# Check if API key is provided before proceeding
if not user_api_key:
    st.warning("Please enter your Gemini API key in the sidebar to start chatting.")
    st.stop()

# Initialize the Google Genai client with the user's provided key
try:
    client = genai.Client(api_key=user_api_key)
except Exception as e:
    st.error(f"Invalid API client initialization: {e}")
    st.stop()

# initialize chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

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
