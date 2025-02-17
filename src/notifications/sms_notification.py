from twilio.rest import Client
from src.config.settings import ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE, RECIPIENT_PHONE

def send_sms(body):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_=TWILIO_PHONE,
        to=RECIPIENT_PHONE,
        body=body
    )
    return message.status
