import math, os
import numpy as np
from datetime import datetime as dt
from numpy import linalg as la
from PIL import Image
from celery import shared_task
from .config import create_app

flask_app = create_app()
celery_app = flask_app.extensions["celery"]

PATH = os.path.dirname(os.path.realpath(__file__))
MIN = 0.000000002
MODELO = np.load(PATH + r'\\H-1.npy')
IMG_SIZE = 60

def erro_maior_que_minimo(q, r):
    # ϵ=||ri+1||2−||ri||2
    if (q == r).all(): return True
    erro = math.fabs(la.norm(r) - la.norm(q))
    return erro >= MIN

@shared_task(ignore_result=False)
def gerar_imagem(file, user):
    inicio = dt.now().strftime('%d-%m-%Y_%H-%M-%S')
    sinal = np.fromstring(file,sep=os.linesep)
    img = np.zeros(IMG_SIZE*IMG_SIZE) # f0=0
    r = q = sinal - np.matmul(MODELO, img) # r0=g−Hf0

    mod_transp = np.transpose(MODELO)
    z = np.matmul(mod_transp, r) # z0=HTr0
    p = z # p0=z0

    i = 0
    while erro_maior_que_minimo(q, r): # for i=0,1,...,until convergence
        i += 1
        w = np.matmul(MODELO, p) # wi=Hpi
        a = np.divide(la.norm(z)**2, la.norm(w)**2) # αi=||zi||22/||wi||22
        img = np.add(img, a*p) # fi+1=fi+αipi
        q = r
        r = np.subtract(r, a*w) # ri+1=ri−αiwi
        z2 = np.matmul(mod_transp, r) # zi+1=HTri+1
        b = np.divide(la.norm(z2)**2, la.norm(z)**2) # βi=||zi+1||22/||zi||22
        p = np.add(z2, b*p) #pi+1=zi+1+βipi
        z = z2

    fim = dt.now().strftime('%d-%m-%Y_%H-%M-%S')
    img = np.reshape(img, (IMG_SIZE,IMG_SIZE), 'F')
    img *= 255
    img = Image.fromarray(img.astype(np.uint8), 'L')
    img.save(f"images/CGNR_60x60_{user}_{inicio}_{fim}_i{i}.png")
    return 'Yey'