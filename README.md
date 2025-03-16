# 🤖 Google Gemini AI Chatbot with Streamlit

## 🚀 Overview
This project is a **Streamlit-based chatbot** powered by **Google Gemini AI**. It allows users to interact with an AI assistant that provides insights on AI, health, and technology.

---

## 🎯 Features
✅ **Real-time AI Chat** - Engage in dynamic conversations with **Google Gemini AI**.
✅ **Google API Integration** - Uses **Gemini-1.5-pro** for intelligent responses.
✅ **Streamlit UI** - Simple and interactive user interface.
✅ **Session Persistence** - Maintains chat history within a session.
✅ **Error Handling** - Displays appropriate messages for missing API keys and failed responses.

---

## 🏗️ Tech Stack
🔹 **Frontend:** Streamlit  
🔹 **Backend:** Python  
🔹 **AI Model:** Google Gemini AI  
🔹 **Environment Management:** dotenv

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
```

### 2️⃣ Create a Virtual Environment & Activate
```bash
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Rename `.env.example` to `.env` and add your **Google API Key**:
```
GOOGLE_API_KEY=your_api_key_here
```

### 5️⃣ Run the Chatbot
```bash
streamlit run app.py
```

---

## 📂 Project Structure
```
📦 gemini-chatbot
 ┣ 📜 app.py                # Main Streamlit application
 ┣ 📜 requirements.txt      # Dependencies
 ┣ 📜 .env.example          # Environment variables template
 ┗ 📜 README.md             # Project documentation
```

---

## 🚀 Usage
1️⃣ Start the application using `streamlit run app.py`.  
2️⃣ Enter a message in the chat input field.  
3️⃣ The AI will generate a response and maintain chat history within the session.  
4️⃣ If the API key is missing or incorrect, an error message will be displayed.

---

## 📌 To-Do
- [ ] Enhance UI with custom themes & animations.
- [ ] Support voice input & text-to-speech response.
- [ ] Implement multi-language support.
- [ ] Add API rate limit handling.

---

## 💡 Contributing
Contributions are welcome! Feel free to fork this repo, create a branch, and submit a **pull request**.

---

## 📜 License
📜 This project is licensed under the **MIT License**.

---

## ✨ Credits
Developed by **Mohammed Mishal** | Powered by **Google Gemini AI** ❤️

