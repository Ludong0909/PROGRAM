import numpy as np
import sympy as sym

def equation(x):
    y = (x**2 + x**0.5) * np.cos(x) / np.sin(x)
    return y

# Sympy solution
x = sym.Symbol('x')
fx =  (x**2 + x**0.5) * sym.cos(x) / sym.sin(x)
f = sym.lambdify(x, fx, 'numpy')  # Convert the sympy function to a numpy-compatible function
df = sym.lambdify(x, sym.diff(fx), 'numpy')

# two point central
def Two_point_central (f, x1, x2):
    '''
    Args:
        f: target equation \n
        x1 > x2
    Returns:
        diff at x
    '''
    deltax = x1 - x2
    tpc = (f(x1) - f(x2)) / (deltax)
    return tpc

# four point central
def Four_point_central (f, x1, x2, x3, x4):
    '''
    Args:
        f: target equation \n
        x1 > x2 > x3 > x4
    Returns:
        diff at x
    '''
    deltax = x2 - x3
    fpc = (f(x4) - 8 * f(x3) + 8 * f(x2) - f(x1)) / (6 * deltax)
    return fpc

tpc = Two_point_central(equation, 2.02, 1.98)
fpc = Four_point_central(equation, 2.04, 2.02, 1.98, 1.96)
stander = df(2)
print(df(2))
print(tpc)
print(fpc)

print((tpc - stander)/stander * 100)
print((fpc - stander)/stander * 100)