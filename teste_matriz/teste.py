import numpy as np

#print(np.show_config())

file = open('a.csv','rb')
a = np.loadtxt(file,delimiter=';')

file = open('M.csv','rb')
M = np.loadtxt(file,delimiter=';')

file = open('N.csv','rb')
N = np.loadtxt(file,delimiter=';')

file = open('aM.csv','rb')
aM = np.loadtxt(file,delimiter=';')

file = open('MN.csv','rb')
MN = np.loadtxt(file,delimiter=';')

result = np.matmul(a,M)
print(result, '\n')
print(aM, '\n')

result = np.matmul(M,N)
print(result, '\n')
print(MN, '\n')