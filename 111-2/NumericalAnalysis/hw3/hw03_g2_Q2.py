import numpy as np
import sympy as sym
import time

# Q2 Applied secant method in meteorology

# set parameters
epsilon = 0.622
A, B = 2.53e9, 5420
K = 7/2

# set tolerance
TOL = 1e-6

# define function Tc
def Solve_Tc(initial):
    w = 10e-3; p0 = 1000; T0 = 300
    Tc = initial
    sol = Tc - B/(np.log(((A*epsilon)/(w*p0))*((T0/Tc)**K)))
    return sol
            
# define function of secant method
def SecantMethod (f, x0, x1, tolerance = 1e-6):

    i = 0
    while (abs(x0-x1)>=tolerance):
        i += 1
        x2 = x1 - f(x1)*(x0-x1)/(f(x0)-f(x1))
        x0 = x1
        x1 = x2
        print('in iterate: ',i ,'current root is: ',(x0 + x1)/2)
    return (x0 + x1)/2

# define bisection method
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

# using secant method solving Tc and print the iteration
start_time = time.time()
Tc_secant = SecantMethod(Solve_Tc, 200, 300, TOL)
end_time = time.time()
print('excecution time: ',end_time - start_time)
print(Tc_secant)

# using bisection method solving Tc and print the iteration
start_time = time.time()
Tc_bisection = BisectionMethod(Solve_Tc, 200, 300, TOL)
end_time = time.time()
print('excecution time: ',end_time - start_time)
print(Tc_bisection)

#----------------------------------------------------------
# using newton method
w = 10e-3; p0 = 1000; T0 = 300
Tc = 200

# define Tc functio
Tc = sym.Symbol('x')
f = Tc - B/(sym.log(((A*epsilon)/(w*p0))*((T0/Tc)**K)))

# Assist By ChatGPT
def newton_method(sympy_func, x0, tolerance = 1e-6):

    # Define symbol and recieved "sympy" function, compute the first derivitive
    x = sym.symbols('x')
    f = sym.lambdify(x, sympy_func, 'numpy')
    df = sym.lambdify(x, sym.diff(sympy_func), 'numpy')
    
    i = 0

    while abs(f(x0)) > tolerance:
        i += 1
        x0 -= f(x0) / df(x0)
        print('current ans: ', x0, ' iteration: ', i+2)
    return x0

sol3 = newton_method(f,300)
print(sol3)

