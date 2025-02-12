import numpy as np
import requests
import json

file = open('G-1.csv','rb')

HEADERS = {'Content-Type': 'application/json', 'Accept':'application/json'}
VALUES = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}

def enviar_sinal():
    files = { 'file': file}
    r = requests.post("http://localhost:5000/", files=files, data=VALUES)
    print(r.content)

enviar_sinal()