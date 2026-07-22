#  Gemini 3.5 Flash-Lite ChatBot

An interactive, web-based conversational AI application built with Streamlit and powered by Google's Gemini API (google-genai SDK). This application allows users to input their own Gemini API key directly into the sidebar to chat with the model while preserving session context throughout the conversation.

---

##  Features

* ** User-Provided API Keys:** Users securely input their own Gemini API key directly via the sidebar interface.
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
```
# Getting Started (Local Setup)

Follow these steps to run the application on your local machine:

1. Prerequisites
Ensure you have Python 3.9+ installed and get a free Gemini API key from Google AI Studio.

2. Clone the Repository
```Bash
git clone [https://github.com/Painx9/Gen_AI.git](https://github.com/Painx9/Gen_AI.git)
cd Gen_AI/Gemini-3.5_Chat_Bot
```
3. Install Dependencies
```Bash
pip install -r requirements.txt
```
5. Run the Application
```Bash
streamlit run main.py
```
Your browser will automatically open a tab at http://localhost:8501.

# Deploying to Streamlit Community Cloud
To share your chatbot online with others:

Push your project folder (```Gemini-3.5_Chat_Bot```) to GitHub (do not upload ```config.json```).

Log in to Streamlit Community Cloud with your GitHub account.

Click New app and configure:

Repository: ```Painx9/Gen_AI```

Branch:```main```

Main file path: ```Gemini-3.5_Chat_Bot/main.py```

Click Deploy!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
