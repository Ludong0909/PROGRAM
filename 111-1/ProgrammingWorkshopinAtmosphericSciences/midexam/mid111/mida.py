import numpy as np

X = np.zeros(10)
Y = np.zeros(10)
n = np.arange(0,10)

X[0] = float(input('input x0 '))
Y[0] = float(input('input y0 '))

A = 0.845
B = 0.035
C = 0.000
D = -0.030
E = 0.820
F = 1.600

for i in range(9):
    X[i+1] = A * X[i] + B * Y[i] +C
    Y[i+1] = D * X[i] + E * Y[i] +F
data = np.column_stack((n,X,Y))
np.savetxt('mida.txt',data,header='n X     Y    ',fmt = ('%3i%6.3f%6.3f') )

