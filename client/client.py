import requests
import os, random
from datetime import datetime as dt
from time import sleep

PATH = os.path.dirname(os.path.realpath(__file__))
USUARIOS = ['user1', 'user2', 'user3', 'user4', 'user5']

def enviar_sinal(user = 'userx', ):
    file = open(PATH + r'\\G-1.csv','rb')
    r = requests.post("http://localhost:5000/", files={'file': file}, 
        data={'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short', 'user': user})

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

random.seed()

while True:
    enviar_sinal(USUARIOS[random.randint(0,4)])
    # sleep(random.randint(1, 5))
    sleep(5)

enviar_sinal(USUARIOS[random.randint(0,4)])