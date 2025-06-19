import os
from dotenv import load_dotenv
import pydantic

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACEHUB_API_KEY = os.getenv("HUGGINGFACEHUB_API_KEY")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
REQUIRE_SIGNATURE = os.getenv("REQUIRE_SIGNATURE", "false").lower() == "true"

COMPANY_KNOWLEDGE_PATH = os.getenv("COMPANY_KNOWLEDGE_PATH", "./data/faqa.txt")

PORT = int(os.getenv("PORT", "8080"))
if PORT in [8000, 4400]:
    PORT = 8081

RELOAD = os.getenv("RELOAD", "false").lower() == "true"

FALLBACK_RESPONSE = os.getenv(
    "FALLBACK_RESPONSE",
    "Sorry, I'm having trouble right now. Please try again later."
)
