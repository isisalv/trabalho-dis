import numpy as np
from numpy import linalg as la
from PIL import Image

'''
g => sinal
H => modelo
'''

'''
f0=0

r0=g−Hf0

z0=HTr0

p0=z0

for i=0,1,...,until convergence

	wi=Hpi

	αi=||zi||22/||wi||22

	fi+1=fi+αipi

	ri+1=ri−αiwi

	zi+1=HTri+1

	βi=||zi+1||22/||zi||22

	pi+1=zi+1+βipi

'''

IMG_SIZE = 60
LOOP = 200

file = open('G-1.csv','rb')
sinal = np.loadtxt(file,delimiter=',')

#file = open('H-1.csv','rb')
#modelo = np.loadtxt(file,delimiter=',')
#np.save('H-1', modelo)
modelo = np.load('H-1.npy')

img = np.zeros(IMG_SIZE*IMG_SIZE) # f0=0
r = sinal - np.matmul(modelo, img) # r0=g−Hf0

mod_transp = np.transpose(modelo)
z = np.matmul(mod_transp, r) # z0=HTr0
p = z # p0=z0

for i in range(0, LOOP): # for i=0,1,...,until convergence
    w = np.matmul(modelo, p) # wi=Hpi
    a = np.divide(la.norm(z)**2, la.norm(w)**2) # αi=||zi||22/||wi||22
    img = np.add(img, a*p) # fi+1=fi+αipi
    r = np.subtract(r, a*w) # ri+1=ri−αiwi
    z2 = np.matmul(mod_transp, r) # zi+1=HTri+1
    b = np.divide(la.norm(z2)**2, la.norm(z)**2) # βi=||zi+1||22/||zi||22
    p = np.add(z2, b*p) #pi+1=zi+1+βipi
    z = z2

img = np.reshape(img, (IMG_SIZE,IMG_SIZE), 'F')
img *= 255
img = Image.fromarray(img.astype(np.uint8), 'L')
img.save(f'image-{LOOP}.png')
img.show()
np.savetxt(f"matrix-{LOOP}.csv", img, delimiter=",")
