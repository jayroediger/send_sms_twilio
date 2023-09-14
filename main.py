#!pip install twilio
from twilio.rest import Client
from config import account_sid, auth_token, my_twilio_phone, to_phone

client = Client(account_sid, auth_token)

message_body = "Goodmorning, Jay. This is a message from Twilio."
message = client.messages \
    .create(
         body= message_body,
         from_= my_twilio_phone,
         to= to_phone
     )

if message.sid:
    print("Message sent successfully.")
else:
    print("There was an error. Message not sent.")