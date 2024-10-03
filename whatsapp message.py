from twilio.rest import Client
import time

# Your Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_whatsapp_number = 'whatsapp:+your_twilio_number'

# Create a Twilio client
client = Client(account_sid, auth_token)

def send_whatsapp_message(to, message):
    try:
        message = client.messages.create(
            body=message,
            from_=twilio_whatsapp_number,
            to=f'whatsapp:{to}'
        )
        print(f'Message sent: {message.sid}')
    except Exception as e:
        print(f'Error sending message: {e}')

if __name__ == "__main__":
    recipient_number = 'recipient_whatsapp_number'  # e.g., 'whatsapp:+1234567890'
    message = 'Hello! This is a test message.'

    while True:
        send_whatsapp_message(recipient_number, message)
        time.sleep(60)  # Sleep for 60 seconds to avoid spamming
