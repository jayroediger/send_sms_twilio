#!pip install twilio
from twilio.rest import Client
from config import *

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_= my_twilio_phone,
         to= to_phone
     )

if message.sid:
    print("Message sent successfully.")
else:
    print("There was an error. Message not sent.")