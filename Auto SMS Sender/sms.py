import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

KEY = os.getenv('KEY')
TOKEN = os.getenv('TOKEN')

account_sid = KEY
auth_token = TOKEN
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12029493890',
    body='And yaa it\'s working.',
    to='+919717209558'
)

print(message.sid)
