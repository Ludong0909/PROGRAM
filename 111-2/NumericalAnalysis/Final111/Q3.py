import numpy as np
import matplotlib.pyplot as plt
import Cheers

# Set parameters
Au = 0.5
Ab = 0.2
Aw = 0.7
D = 0.3
Topt = 295.5
Tmin = 283
Tmax = 313
sigma = 5.67e-8
cins = 0.2
Fsun = 3668

# (a.) solve albedo
def Slove_Albedo(Su, Sb, Sw):
    return Su*Au + Sw*Aw + Sb*Ab

Ap = Slove_Albedo(0.2,0.3,0.5)
print(Ap)

# (b.) solve temp.
def Fx(Ax):
    return Fsun * (1-Ax)/4

Fp = Fx(Ap)
Fw = Fx(Aw)
Fb = Fx(Ab)

def Solve_Temperature(Fx):
    return (cins*(Fx-Fp)/sigma + Fp/sigma)**0.25

Tp = Solve_Temperature(Fp)
Tw = Solve_Temperature(Fw)
Tb = Solve_Temperature(Fb)

# (c.) 
def G (Tw):
    if Tmin <= Tw and Tw <= Tmax:
        return 1 - ((Tw - Topt)/(Tmin - Tmax))**2
    else:
        return 0

Sw = np.zeros(40 + 1)
Sb = np.zeros(40 + 1)
Sw[0] = 0.01
Sb[0] = 0.01


for i in range(1, 41):
    Su = 1 - Sb[i-1] - Sw[i-1]
    Ap = Slove_Albedo(Su, Sb[i-1], Sw[i-1])
    
    Fp = Fx(Ap)
    Fw = Fx(Aw)
    Fb = Fx(Ab)

    Tp = Solve_Temperature(Fp)
    Tw = Solve_Temperature(Fw)
    Tb = Solve_Temperature(Fb)

    Sw[i] = Sw[i-1] + Sw[i-1] * (G(Tw)*Sw[i-1] - D)
    Sb[i] = Sb[i-1] + Sb[i-1] * (G(Tb)*Sb[i-1] - D)

    if Sw[i] < 0.01:
        Sw[i] = 0.01
    if Sb[i] < 0.01:
        Sb[i] = 0.01

Sp = Sw + Sb

plt.plot(Sp)
plt.plot(Sw)
plt.plot(Sb)
plt.legend(['Sp', 'Sw', 'Sb'])
plt.xlabel('Generation')
plt.ylabel('Population')
plt.title('Population v.s. Generation')
plt.grid()
plt.show()