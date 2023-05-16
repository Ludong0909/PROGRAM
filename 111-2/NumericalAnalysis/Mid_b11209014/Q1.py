import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import Cheers

def sol_Tw (Tinitial):
    epscilon = 0.622
    A, B = 2.53e9, 5420
    Cp = 1004
    Lv = 2.5e6
    T0 = 300
    P0 = 1000
    w = 10e-3
    Tw = float(Tinitial)
    sol = T0 - Lv/Cp*(epscilon/P0 * A * np.exp(-B/Tw)-w)-Tw

    return sol

epscilon = 0.622
A, B = 2.53e9, 5420
Cp = 1004
Lv = 2.5e6
T0 = 300
P0 = 1000
w = 10e-3
Tw = sym.Symbol('x')
f = T0 - (Lv/Cp)*((epscilon/P0) * A * sym.exp(-B/Tw)-w)-Tw

bi_sol = Cheers.BisectionMethod(sol_Tw, 200, 500, 1e-7)
nt_sol = Cheers.NewtonMethod(f, 500, 1e-7)
sec_sol = Cheers.SecantMethod(sol_Tw, 300, 500, 1e-7)

print('bisection method =',bi_sol)
print('newton method =',nt_sol)
print('secant method =',sec_sol)