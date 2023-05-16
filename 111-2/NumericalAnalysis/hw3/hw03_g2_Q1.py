import scipy.optimize as opt
import numpy as np
import sympy as sym

# Set tolerance
TOL = 1e-6

# Define target function
def func(x):
    y = 2*np.sin(x)-1/4*np.exp(x)-1
    return y

# Define sympy form of function
x = sym.Symbol('x')
f = 2*sym.sin(x)-1/4*sym.exp(x)-1

# Using function fsolve (newton method)
sol1 = opt.fsolve(func, -5)

# Define bisection method
def BisectionMethod (f, x1, x2, tolerance = 1e-6):
    i = 0
    if (x1<x2) and (f(x1)*f(x2)) < 0 :
        while (x2-x1)>=tolerance:
            i += 1
            x3 = (x2+x1)/2
            if (f(x1)*f(x3)) < 0 :
                x2 = x3
            elif(f(x1)*f(x3)) > 0:
                x1 = x3
            elif(f(x3) == 0):
                return x3
            else:
                print('Error')
                return 0
            print('current ans= ', (x1+x2)/2, ' ,iterate times: ', i)
        return ((x1+x2)/2)
    elif(f(x1)==0):
        return x1
    elif(f(x2)==0):
        return x2
    else:
        print('Invalid Input')
        return 0
sol2 = BisectionMethod(func, -6, -5, TOL)

# Written By ChatGPT
def newton_method(expr, x0, tolerance, max_iter=100):

    x = sym.symbols('x')
    f = sym.lambdify(x, expr, 'numpy')
    df = sym.lambdify(x, sym.diff(expr, x), 'numpy')
    
    for i in range(max_iter):
        fx = f(x0)
        if abs(fx) < tolerance:
            return x0
        dfx = df(x0)
        x0 -= fx / dfx
        print('current ans: ', x0, ' iteration: ', i+2)
    raise ValueError("Failed to converge after {} iterations".format(max_iter))
sol3 = newton_method(f,-7,TOL,100)
print(sol3)

# Define secant method 
def SecantMethod (f, x0, x1, tolerance = 1e-6):
    i = 0
    while (abs(x0-x1)>=tolerance):
        i += 1
        x2 = x1 - f(x1)*(x0-x1)/(f(x0)-f(x1))
        x0 = x1
        x1 = x2
        print('in iterate: ',i ,' ,current root is: ',(x0 + x1)/2)
    return (x0 + x1)/2
sol4 = SecantMethod(func, 0, 1)
print(sol4)