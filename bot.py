from lxml import html
import requests

import json
import random
import time

from pprint import pprint

import os
from slackclient import SlackClient


if ('SLACK_BOT_TOKEN' in os.environ):
	speed = 1
else:
	speed = 0

def send(str):
	if ('SLACK_BOT_TOKEN' in os.environ):
		slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
		slack_client.api_call("chat.postMessage", channel="geneva", text=str, as_user=True)
	else:
		pprint(str)

with open('data.json') as data_file:
	data = json.load(data_file)

i = random.randrange(len(data))

send(str(i) + ": " + data[i]['Categorie'] + "/" + data[i]['SousCategorie'])

send(data[i]['Question'])

time.sleep(10*speed)

a = random.randrange(1, 4)

send(data[i]['Reponse'+str(a)])
b = 2
if (a == 2):
	b = 1
time.sleep(1*speed)
send(data[i]['Reponse'+str(b)])
c = 3
if (a == 3):
	c = 1
time.sleep(1*speed)
send(data[i]['Reponse'+str(c)])

time.sleep(20*speed)
send("Reponse: " + data[i]['Reponse1'])
send(data[i]['Anecdote'])
send(data[i]['Media'])
