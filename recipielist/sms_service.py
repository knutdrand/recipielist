import os

from twilio.rest import Client

# Twilio credentials
twilio_number = "+13149484399"
my_number = "+4793436159"  # Your Norwegian number
account_sid, auth_token = os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)


def send_sms_to_me(body):
    message = client.messages.create(
        body=body,
        from_=twilio_number,
        to=my_number
    )
    print("Message sent! SID:", message.sid)


if __name__ == "__main__":
    body = "Hello, this is a test SMS from Python!"
    send_sms_to_me(body)
