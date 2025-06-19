from fastapi import FastAPI, Request, Form
from fastapi.responses import PlainTextResponse
from app.chatbot_logic import get_response
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Phymaco WhatsApp Agent is working!"}


@app.post("/webhook")
async def whatsapp_webhook(
    Body: str = Form(...), 
    From: str = Form(...)
):
    print("📥 Incoming WhatsApp Message:", Body, "From:", From)  
    try:
        answer = get_response(Body)
        print("🤖 Answer from get_response():", answer)  

        reply = f"<Response><Message>{answer}</Message></Response>"
        print(" TwiML Reply Sent:", reply)  
        return PlainTextResponse(content=reply, media_type="application/xml")
    except Exception as e:
        print(" Error in webhook:", e)
        fallback = " Sorry, Phymaco's assistant is temporarily busy. Try again soon."
        return PlainTextResponse(content=f"<Response><Message>{fallback}</Message></Response>", media_type="application/xml")


@app.post("/status")
async def status_callback(request: Request):
    data = await request.form()
    print("📦 Status Callback:", data)
    return {"status": "ok"}



if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
