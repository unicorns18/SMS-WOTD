from random_word import RandomWords
from twilio.rest import Client
import time
import json

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def dailyWOTD():
  r = RandomWords()
  word = r.word_of_the_day()
  parsed_json = json.loads(word)
  message_body = parsed_json['definations'][0]['text']

  message = client.messages.create(
                                body=message_body,
                                from_='+1', # Add your twilio phone number
                                to='+1' # Add your phone number or the one you want to send them to
                            )

while True:
    if time.localtime().tm_hour == 19  and time.localtime().tm_min == 0: # It uses military time, be aware. (0-23)
        dailyWOTD()
