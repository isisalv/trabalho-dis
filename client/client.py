import numpy as np
import requests
import json
import os
from datetime import datetime as dt

PATH = os.path.dirname(os.path.realpath(__file__))

file = open(PATH + r'\\G-1.csv','rb')

HEADERS = {'Content-Type': 'application/json', 'Accept':'application/json'}
VALUES = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short', 'user': 'isis'}

def enviar_sinal():
    r = requests.post("http://localhost:5000/", files={'file': file}, data=VALUES)

    print(f"[{ dt.now().strftime('%d/%m/%Y %H:%M:%S') }]")
    print(f" Uso da CPU: { r.json()['cpu'] }%")
    print(f" Uso de Memória: { r.json()['ram'] }% \n")

enviar_sinal()