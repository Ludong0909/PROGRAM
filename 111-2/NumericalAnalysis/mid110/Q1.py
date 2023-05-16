import numpy as np
import sympy as sym

# 1.1
def BisectionMethod(f, x1, x2, tolerance=1e-6):
    i = 0  # Initialize iteration counter
    if (x1 < x2) and (f(x1) * f(x2)) < 0:  # Check if the function values at x1 and x2 have opposite signs
        while (x2 - x1) >= tolerance:  # Loop until the interval between x1 and x2 is smaller than the tolerance
            i += 1  # Increment iteration counter
            x3 = (x2 + x1) / 2  # Compute the midpoint of x1 and x2
            if (f(x1) * f(x3)) < 0:  # Check if the function values at x1 and x3 have opposite signs
                x2 = x3  # Update x2 to x3
            elif (f(x1) * f(x3)) > 0:  # Check if the function values at x1 and x3 have the same sign
                x1 = x3  # Update x1 to x3
            elif (f(x3) == 0):  # Check if x3 is a root (i.e., f(x3) = 0)
                return x3  # Return the root
            else:
                print('Error')  # Print an error message if none of the above conditions are met
                return 0
            print('current ans= ', (x1 + x2) / 2, ' ,iterate times: ', i)  # Print the current approximation and iteration count
        return ((x1 + x2) / 2)  # Return the final approximation
    elif (f(x1) == 0):  # Check if x1 is a root (i.e., f(x1) = 0)
        return x1  # Return x1 as the root
    elif (f(x2) == 0):  # Check if x2 is a root (i.e., f(x2) = 0)
        return x2  # Return x2 as the root
    else:
        print('Invalid Input')  # Print an error message if the input is invalid
        return 0

# Assist by ChatGPT
def NewtonMethod(sympy_func, x0, tolerance=1e-6):
    """
    Newton's Method for finding the root of a function.

    Parameters:
        - sympy_func (sympy.Basic): Sympy function representing the function whose root needs to be found.
        - x0 (float): Initial approximation for the root.
        - tolerance (float, optional): Tolerance for convergence. Defaults to 1e-6.

    Returns:
        - float: Approximation of the root found.
    """

    import sympy as sym  # Import the sympy library for symbolic computing

    # Define symbol and received "sympy" function, compute the first derivative
    x = sym.symbols('x')  # Define x as a symbolic variable
    f = sym.lambdify(x, sympy_func, 'numpy')  # Convert the sympy function to a numpy-compatible function
    df = sym.lambdify(x, sym.diff(sympy_func), 'numpy')  # Compute the first derivative of the sympy function and convert to a numpy-compatible function

    i = 0  # Initialize iteration counter

    while abs(f(x0)) > tolerance:  # Loop until the absolute value of the function at x0 is smaller than the tolerance
        i += 1  # Increment iteration counter
        x0 -= f(x0) / df(x0)  # Update x0 using the Newton's Method formula
        print('current ans: ', x0, ' iteration: ', i + 2)  # Print the current approximation and iteration count
    return x0  # Return the final approximation of the root

x = sym.Symbol('x')
f = sym.sin(x)

def f_sin (x):
    return np.sin(x)

ans1 = BisectionMethod(f_sin, 2.4, 3.4, tolerance=1e-7)
ans2 = NewtonMethod(f, 3.1, tolerance=1e-7)

print(ans1)
print(ans2)

