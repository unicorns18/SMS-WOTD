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
  message_body_word = parsed_json['word']
  message_body_def = parsed_json['definations'][0]['text']
  message_body = 'Word: ' + message_body_word + ' - ' + 'Definition: ' + message_body_def

  message = client.messages.create(
                                body=message_body,
                                from_='+12133363631',
                                to='+17086651159'
                            )

while True:
    if time.localtime().tm_hour == 19  and time.localtime().tm_min == 0:
        dailyWOTD()
