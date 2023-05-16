# import required libraries
import numpy as np
import sympy as sp

# define a function to find root using the Bisection method
def BisectionRoot(f, target=0, x1=0, x2=1, Tolerance=1e-6):
    # initialize counter
    i = 1
    
    # check if the interval is valid and contains a root
    if ((x1<x2) and (f(x1)*f(x2))<0):
        # iterate until tolerance level is reached
        while ((x2-x1) >= Tolerance):
            # calculate midpoint of the interval
            x3 = (x1+x2)/2
            
            # check which side of the interval the root is on and update the interval accordingly
            if ((f(x1)*f(x3)) < 0):
                x2 = x3
                # print current iteration and the midpoint
                print("    Finding Bisection Root #%i, currently at" %i, x2)
            elif ((f(x1)*f(x3)) > 0):
                x1 = x3
                # print current iteration and the midpoint
                print("    Finding Bisection Root #%i, currently at" %i, x1)
            elif (f(x3) == 0):
                return x3
            else:
                print("Some error occurred")
                return 0
            i += 1
        return (x1+x2)/2
    # check if the endpoints themselves are roots
    elif (f(x1) == 0):
        return x1
    elif (f(x2) == 0):
        return x2
    else:
        print("Invalid input: x1 and x2 are in the same sign")
        return 0

# define a function to find root using the Newton-Raphson method
def NewtonRoot (f, df, x1=1, TOL=1e-6):
    # initialize counter
    i = 1
    
    # calculate the first iteration
    x2 = x1-f(x1)/df(x1)
    # print current iteration and the new value of x
    print("    Finding Newton Root #%i, currently at" %i, x2)
    
    # iterate until the tolerance level is reached
    while (abs(x2-x1) > TOL):
        x1 = x2
        x2 = x1-f(x1)/df(x1)
        i += 1
        # print current iteration and the new value of x
        print("    Finding Newton Root #%i, currently at"%i, x2)
    
    return x2

# define the function whose root we want to find and its derivative
def f(x):
    return 2*np.sin(x)-np.exp(x)/4-1

def df(x):
    return 2*np.cos(x)-np.exp(x)/4

# ------------------------------------------------------------------
# set the tolerance levels
TOL1 = 1e-6
TOL2 = 1e-10

# Find a root of f(x) using the bisection method with tolerance TOL1
BRoot = BisectionRoot(f, target=0, x1=-7, x2=-4, Tolerance=TOL1)
print("Bisection Root: ", BRoot, "\nTOL =", TOL1)

# Find roots of f(x) using the Newton-Raphson method with tolerance TOL1 and initial guesses -7, -5, and -3
for i in ([-7, -5, -3]):
    NTRoot = NewtonRoot(f, df, x1=i, TOL=TOL1)
    print("Newton Root with initial guess", i, ": ", NTRoot, "\nTOL =", TOL1)

# Find a root of f(x) using the bisection method with tolerance TOL2
BRoot = BisectionRoot(f, target=0, x1=-7, x2=-4, Tolerance=TOL2)
print("Bisection Root: ", BRoot, "\nTOL =", TOL2)

# Find roots of f(x) using the Newton-Raphson method with tolerance TOL2 and initial guesses -7, -5, and -3
for i in ([-7, -5, -3]):
    NTRoot = NewtonRoot(f, df, x1=i, TOL=TOL2)
    print("Newton Root with initial guess", i, ": ", NTRoot, "\nTOL =", TOL2)
    