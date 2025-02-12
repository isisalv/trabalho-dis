import numpy as np
import requests
import json
import os

PATH = os.path.dirname(os.path.realpath(__file__))

file = open(PATH + r'\\G-1.csv','rb')

HEADERS = {'Content-Type': 'application/json', 'Accept':'application/json'}
VALUES = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short', 'user': 'isis'}

def enviar_sinal():
    files = { 'file': file}
    r = requests.post("http://localhost:5000/", files=files, data=VALUES)
    print(r.content)

enviar_sinal()