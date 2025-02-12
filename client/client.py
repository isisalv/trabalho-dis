import requests
import os
from datetime import datetime as dt

PATH = os.path.dirname(os.path.realpath(__file__))

file = open(PATH + r'\\G-1.csv','rb')

HEADERS = {'Content-Type': 'application/json', 'Accept':'application/json'}
VALUES = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short', 'user': 'isis'}

def enviar_sinal():
    r = requests.post("http://localhost:5000/", files={'file': file}, data=VALUES)

    if r.status_code == 200:
        print(f"[{ dt.now().strftime('%d/%m/%Y %H:%M:%S') }]")
        print(f" Result ID: { r.json()['result_id'] }%")
        print(f" Uso da CPU: { r.json()['cpu'] }%")
        print(f" Uso de Memória: { r.json()['ram'] }% \n")
    else:
        print("Erro")

def get_result():
    r = requests.get("http://localhost:5000/24809e80-dc58-409f-af17-f364f57362e6%")
    print(r.content)

enviar_sinal()
# get_result()