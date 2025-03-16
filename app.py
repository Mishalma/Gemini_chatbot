import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key from environment
API_KEY = os.getenv("GOOGLE_API_KEY")

# Ensure API key is set
if not API_KEY:
    st.error("❌ Google API Key is missing! Please set it in your environment variables.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Select a valid model from the available list
MODEL_NAME = "gemini-1.5-pro"  # Change to "gemini-1.5-flash" for faster responses

try:
    model = genai.GenerativeModel(MODEL_NAME)
except Exception as e:
    st.error(f"❌ Failed to load model '{MODEL_NAME}'. Error: {e}")
    st.stop()

# Function to convert Gemini roles to Streamlit roles
def role_to_streamlit(role):
    return "assistant" if role == "model" else role

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display app title
st.title("🤖 Chat with Google Gemini!")

# Show chat history
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# User input & AI response handling
if prompt := st.chat_input("Ask me anything about AI, health, or tech!"):
    # Display user message
    st.chat_message("user").markdown(prompt)

    try:
        # Get AI response
        response = st.session_state.chat.send_message(prompt)

        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(response.text)

    except Exception as e:
        st.error(f"❌ Error while generating response: {e}")
