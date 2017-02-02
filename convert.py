from lxml import html
import requests

import json
import random
import time

from pprint import pprint

import os


with open('data.json') as data_file:
	data = json.load(data_file)

output = {'version': str(time.time()), 'name': 'lejeu', 'questions': []}
for d in data:
    q = {}
    q['text'] = d['Question']
    q['answers'] = []
    q['answers'].append({'text': d['Reponse1'], 'isCorrect': True})
    q['answers'].append({'text': d['Reponse2'], 'isCorrect': False})
    q['answers'].append({'text': d['Reponse3'], 'isCorrect': False})
    output['questions'].append(q)

print json.dumps(output)
