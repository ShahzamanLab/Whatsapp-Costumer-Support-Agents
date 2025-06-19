# Whatsapp-Costumer-Support-Agents

# 🤖 WhatsApp Customer Support Agent

An AI-powered WhatsApp customer support chatbot built using **LangChain**, **FastAPI**, **Twilio**, and **LLMs (like OpenAI or Groq)**. It uses company-specific knowledge (via RAG) to respond intelligently to customer queries through WhatsApp — automatically, instantly, and 24/7.

---

## ✨ Features

- 🔍 Understands customer queries with NLP
- 📚 Retrieval-Augmented Generation (RAG) using your custom company data
- 🤖 Responds smartly using LLMs (OpenAI/Groq)
- 📱 Integrated with WhatsApp via Twilio Webhook
- ⚡ Built with FastAPI and LangChain
- 🧠 Supports FAQs, smart prompts, and fallback options
- 🔄 Easily extendable for appointment booking, ticketing, etc.

---

## 🧠 Tech Stack

| Layer         | Tool/Library            |
|---------------|--------------------------|
| Backend       | Python 3.12, FastAPI     |
| NLP/LLM       | LangChain, OpenAI / Groq |
| Integration   | Twilio WhatsApp API      |
| Data Storage  | TXT / JSON / ChromaDB    |
| Testing       | Pytest                   |

---

## 📁 Project Structure



---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/ShahzamanLab/Whatsapp-Costumer-Support-Agents.git
cd Whatsapp-Costumer-Support-Agents

  Create a Virtual Environment and Install Requirements
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


  ##Configure API Keys

  OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886


#Run the App Locally
uvicorn app.main:app --reload

#Make it Public (Webhook with ngrok)
ngrok http 8000


