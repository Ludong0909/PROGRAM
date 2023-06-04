import numpy as np
import matplotlib.pyplot as plt

k = 0.5

def ODEs_Solve_RK4(ODE_funcs,p0,vars,h):
    
    n = len(vars)
    p = p0
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    k3 = np.zeros(n)
    k4 = np.zeros(n)
    v1 = np.zeros(n)
    v2 = np.zeros(n)
    v3 = np.zeros(n)
    v4 = np.zeros(n)

    for i in range(n):
        k1[i] = ODE_funcs[i](p,*vars)
        v1[i] = vars[i] + k1[i]*h/2
    p = p0 + h/2
    for i in range(n):
        k2[i] = ODE_funcs[i](p,*v1)
        v2[i] = vars[i] + k2[i]*h/2
    p = p0 + h/2
    for i in range(n):
        k3[i] = ODE_funcs[i](p,*v2)
        v3[i] = vars[i] + k3[i]*h
    p = p0 + h
    for i in range(n):
        k4[i] = ODE_funcs[i](p,*v3)
        v4[i] = vars[i] + (k1[i]+2*k2[i]+2*k3[i]+k4[i])*h/6
    
    return tuple(v4)


def dx1dt (t, x1, x2, x3):
    return x1 - 0.001*x1**2 - 0.001*k*x1*x2 - 0.01*x1*x3


def dx2dt (t, x1, x2, x3):
    return x2 - 0.0015*k*x1*x2 - 0.001*x2**2 - 0.001*x2*x3


def dx3dt (t, x1, x2, x3):
    return - x3 + 0.005*x1*x3 + 0.0005*x2*x3

x1_ini = 1000
x2_ini = 300
x3_ini = 400

T = np.linspace(0,50,5001)
x1 = np.ones(5001) * x1_ini
x2 = np.ones(5001) * x2_ini
x3 = np.ones(5001) * x3_ini

for i in range(len(T)):
    x1[i], x2[i], x3[i] = ODEs_Solve_RK4([dx1dt, dx2dt, dx3dt], T[i-1], [x1[i-1], x2[i-1], x3[i-1]], 0.01)

plt.plot(T,x1)
plt.plot(T,x2)
plt.plot(T,x3)
plt.xlim(0,50)
plt.ylim(bottom=0)
plt.legend(['x1', 'x2', 'x3'])
plt.grid()
plt.show()

plt.plot(x1,x2)
plt.grid()
plt.show()

plt.plot(x2,x3)
plt.grid()
plt.show()