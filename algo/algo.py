import numpy as np
from PIL import Image

IMG_SIZE = 60

file = open('G-1.csv','rb')
sinal = np.loadtxt(file,delimiter=',')

#file = open('H-1.csv','rb')
#modelo = np.loadtxt(file,delimiter=',')
#np.save('H-1', modelo)
modelo = np.load('H-1.npy')

img = np.zeros(IMG_SIZE*IMG_SIZE)
r = sinal - np.matmul(modelo, img)

mod_transp = np.transpose(modelo)
z = np.matmul(mod_transp, r)
p = z

for i in range(0,5):
    w = np.matmul(modelo, p)
    mult_r = np.matmul(np.transpose(r),r)
    a = np.divide(mult_r, np.matmul(np.transpose(p),p))
    img = np.add(img, a*p)
    r = np.subtract(r, np.matmul(a*modelo, p))
    b = np.divide(np.matmul(np.transpose(r), r), mult_r)
    p = np.add(np.matmul(mod_transp, r), b*p)

img = np.reshape(img, (IMG_SIZE,IMG_SIZE), 'F')
img *= 255
img = Image.fromarray(img.astype(int), 'L')
img.save('my.png')
img.show()