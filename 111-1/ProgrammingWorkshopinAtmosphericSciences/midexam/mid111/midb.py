import numpy as np
import matplotlib.pyplot as plt

nmax = 10000
Pn = np.random.rand(nmax-1)
X = np.zeros(nmax)
Y = np.zeros(nmax)
X[0] = 0
Y[0] = 0

A1 = 0.000
A2 = 0.845  
A3 = 0.200
A4 = -0.150

B1 = 0.000
B2 = 0.035  
B3 = -0.260
B4 = 0.240

C1 = 0.000
C2 = 0.000
C3 = 0.000
C4 = 0.000

D1 = 0.000
D2 = -0.030
D3 = 0.255
D4 = 0.250

E1 = 0.200
E2 = 0.820
E3 = 0.245
E4 = 0.200

F1 = -0.012
F2 = 1.600
F3 = 0.290
F4 = 0.680

for i in range(0,nmax-1):
    if   (0.00 <= Pn[i]) and (Pn[i] <0.01):
        X[i+1] = A1 * X[i] + B1 * Y[i] +C1
        Y[i+1] = D1 * X[i] + E1 * Y[i] +F1 
    elif (0.01 <= Pn[i]) and (Pn[i]< 0.86):
        X[i+1] = A2 * X[i] + B2 * Y[i] +C2
        Y[i+1] = D2 * X[i] + E2 * Y[i] +F2
    elif (0.86 <= Pn[i]) and (Pn[i] < 0.93):
        X[i+1] = A3 * X[i] + B3 * Y[i] +C3
        Y[i+1] = D3 * X[i] + E3 * Y[i] +F3 
    else :
        X[i+1] = A4 * X[i] + B4 * Y[i] +C4
        Y[i+1] = D4 * X[i] + E4 * Y[i] +F4

plt.plot(X,Y,'go')
plt.savefig('midb.png')
plt.show()

