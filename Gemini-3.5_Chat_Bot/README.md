#  Gemini 3.5 Flash-Lite ChatBot

An interactive, web-based conversational AI application built with **Streamlit** and powered by Google's **Gemini API** (`google-genai` SDK). This chatbot maintains session context across conversations and features secure API key management for both local development and cloud deployment.

---

##  Features

* ** Interactive Chat UI:** Clean and responsive user interface built using Streamlit's native chat components.
* ** Context Awareness:** Keeps track of chat history during your active session to maintain smooth multi-turn conversations.
* ** Powered by Gemini:** Utilizes Google's fast and efficient `gemini-3.5-flash-lite` model for speedy responses.
* ** Secure Configuration:** Handles API keys safely using `st.secrets` on Streamlit Cloud or a local `config.json` file.

---

##  Tech Stack

* **Language:** Python 3.9+
* **Frontend/UI:** [Streamlit](https://streamlit.io/)
* **AI Model/SDK:** [Google GenAI SDK](https://pypi.org/project/google-genai/) (`google-genai`)

---

##  Project Structure

```text
Gemini-3.5_Chat_Bot/
├── main.py              # Main Streamlit application logic
├── requirements.txt     # Python dependencies
├── .gitignore          # Keeps secrets and local environments off GitHub
├── README.md            # Project documentation
└── config.json          # Local API configuration (ignored in Git for security)
