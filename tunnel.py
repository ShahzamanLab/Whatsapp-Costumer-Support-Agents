from pyngrok import ngrok, conf


conf.get_default().auth_token = "your ngork auth token"

public_url = ngrok.connect(8000)


print("✅ Ngrok Tunnel Running!")
print("🌍 Public URL:", public_url)
print("📮 Add this URL to Twilio Sandbox Webhook like: https://abcd1234.ngrok.io/webhook")


input("Press Enter to exit and close the tunnel...")
