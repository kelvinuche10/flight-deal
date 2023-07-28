from twilio.rest import Client


account_sid = your_twilio_sid
auth_token = your_twilio_token
        

class NotificationManager:
    def __init__(self, message)
        client = Client(account_sid, auth_token)

        message = client.messages.create(
          from_='+17624753710',
          body=message,
          to=your_phone_number
        )
