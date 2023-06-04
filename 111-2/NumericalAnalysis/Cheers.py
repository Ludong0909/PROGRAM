import numpy as np
import scipy as sci
import sympy as sym

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


def Factorial(N):
    b = 1  # Initialize the factorial variable to 1
    if (float(N) >= 0.0):  # Check if the input N is a non-negative number
        if (float(N) == 0):  # Check if N is equal to 0
            return 1  # Return 1 as the factorial of 0 is defined as 1
        else:
            if (float(N) % 1 == 0.0):  # Check if N is an integer (i.e., has no decimal part)
                for i in range(1, int(float(N)) + 1):  # Loop from 1 to N (inclusive)
                    b = b * i  # Multiply b by each integer in the range to compute the factorial
                return b  # Return the computed factorial
            else:
                print('the wrong input')  # Print an error message if N is not an integer
    else:
        print('the wrong input')  # Print an error message if N is a negative number


def SecantMethod(f, x0, x1, tolerance=1e-6):
    i = 0  # Initialize iteration counter
    while (abs(x0 - x1) >= tolerance):  # Loop until the absolute difference between x0 and x1 is smaller than the tolerance
        i += 1  # Increment iteration counter
        x2 = x1 - f(x1) * (x0 - x1) / (f(x0) - f(x1))  # Compute the next approximation using the Secant Method formula
        x0 = x1  # Update x0 to x1
        x1 = x2  # Update x1 to x2
        print('in iterate: ', i, ' ,current root is: ', (x0 + x1) / 2)  # Print the current approximation and iteration count
    return (x0 + x1) / 2  # Return the final approximation of the root


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


# Assist by ChatGPT
def TwoEquationSystem(sympy_f1, sympy_f2, x0, y0, tolerance=1e-6):

    # Set symbol and received "sympy" function, compute partial derivative of two functions
    x, y = sym.symbols('x y')  # Define symbols x and y
    f1 = sym.lambdify((x, y), sympy_f1, 'numpy')  # Convert sympy function sympy_f1 to a numpy-compatible lambda function
    fx1 = sym.lambdify((x, y), sym.diff(sympy_f1, x), 'numpy')  # Compute the partial derivative of sympy_f1 with respect to x and convert it to a numpy-compatible lambda function
    fy1 = sym.lambdify((x, y), sym.diff(sympy_f1, y), 'numpy')  # Compute the partial derivative of sympy_f1 with respect to y and convert it to a numpy-compatible lambda function
    f2 = sym.lambdify((x, y), sympy_f2, 'numpy')  # Convert sympy function sympy_f2 to a numpy-compatible lambda function
    fx2 = sym.lambdify((x, y), sym.diff(sympy_f2, x), 'numpy')  # Compute the partial derivative of sympy_f2 with respect to x and convert it to a numpy-compatible lambda function
    fy2 = sym.lambdify((x, y), sym.diff(sympy_f2, y), 'numpy')  # Compute the partial derivative of sympy_f2 with respect to y and convert it to a numpy-compatible lambda function

    i = 0  # Initialize iteration counter

    while (abs(f1(x0, y0)) > tolerance and abs(f2(x0, y0)) > tolerance):
        i += 1  # Increment iteration counter
        jacobian = fx1(x0, y0) * fy2(x0, y0) - fy1(x0, y0) * fx2(x0, y0)  # Compute the Jacobian Matrix
        deltax = (-f1(x0, y0) * fy2(x0, y0) + f2(x0, y0) * fy1(x0, y0)) / jacobian  # Compute the change in x
        deltay = (-f2(x0, y0) * fx1(x0, y0) + f1(x0, y0) * fx2(x0, y0)) / jacobian  # Compute the change in y
        x0 += deltax  # Update x0 with the change in x
        y0 += deltay  # Update y0 with the change in y
        print('current ans: ', x0, y0, ' ,iteration: ', i)  # Print the current approximation and iteration count

    return (x0, y0)  # Return the final approximation of x and y as a tuple


def PartialPivot(A, AX, i):
    """
    Performs partial pivoting on the matrix A and the vector AX
    """
    n = A.shape[0]
    max_index = i
    for j in range(i+1, n):
        if abs(A[j, i]) > abs(A[max_index, i]):
            max_index = j
    if max_index != i:
        A[[i, max_index]] = A[[max_index, i]]
        AX[[i, max_index]] = AX[[max_index, i]]
    return A, AX


# Old one
def Gauss_elim(A, AX):


    def PartialPivot(A, AX, i):
        """
        Performs partial pivoting on the matrix A and the vector AX
        """
        n = A.shape[0]
        max_index = i
        for j in range(i+1, n):
            if abs(A[j, i]) > abs(A[max_index, i]):
                max_index = j
        if max_index != i:
            A[[i, max_index]] = A[[max_index, i]]
            AX[[i, max_index]] = AX[[max_index, i]]
        return A, AX
    

    n = len(AX)
    for i in range(n):
        A, AX = PartialPivot(A, AX, i)
        for j in range(i+1,n):
            AX[j] = AX[j] - AX[i]*(A[j][i]/A[i][i])
            A[j] = A[j] - A[i]*(A[j][i]/A[i][i])
    X = BackwardSub(A,AX)
    return X


# Old one
def BackwardSub(A, AX):
    '''
    Arg: 
        A (NDarray): target coefficient array.
        AX (NDarray): Right-hand array of target array.

    Return:
        X (NDarray): Solved X
    '''
    n = len(AX)
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = (AX[i]-np.dot(A[i][:], X))/A[i][i]
    return X


# Assist by ChatGPT
def Gaussian_Elimination(A, AX):
    """
    Solves a system of linear equations using Gaussian elimination.
    
    Args:
        A: a numpy array representing the coefficient matrix.
        AX: a numpy array representing the right-hand side vector.
    
    Returns:
        x: a numpy array representing the solution vector.
    """
    n = len(A)
    # Augment the coefficient matrix with the right-hand side vector
    M = np.hstack([A, AX.reshape(n, 1)])
    # Gaussian elimination with partial pivoting
    for i in range(n):
        # Find the row with the largest absolute value in column i
        pivot_row = i + np.argmax(np.abs(M[i:, i]))
        # Swap the current row with the pivot row
        M[[i, pivot_row]] = M[[pivot_row, i]]
        # Eliminate the variable in column i for all subsequent rows
        for j in range(i + 1, n):
            factor = M[j, i] / M[i, i]
            M[j, i:] -= factor * M[i, i:]
    # Back-substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, :-1], x)) / M[i, i]
    return x


# Assist by ChatGPT
def Jacobi_iteration(A, AX, x0=None, tol = 0.05, max_iter=1000):
    """
    Solves the system of linear equations Ax = AX using Jacobi iteration method.

    Parameters:
    A (numpy.ndarray): Input matrix of shape (n,n).
    AX (numpy.ndarray): Answer of input matrix of shape (n,).
    x0 (numpy.ndarray, optional): Initial guess for the solution. If None, a zero vector of shape (n,) will be used. Default is None.
    tol (float, optional): Tolerance for convergence. Default is 1e-10.
    max_iter (int, optional): Maximum number of iterations. Default is 1000.

    Returns:
    x (numpy.ndarray): Solution of the system of linear equations of shape (n,).
    num_iter (int): Number of iterations performed.
    """
    n = A.shape[0]
    if x0 is None:
        x0 = np.zeros(n)

    x = x0.copy()
    x_new = np.zeros(n)
    num_iter = 0

    while num_iter < max_iter:
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s += A[i, j] * x[j]
            x_new[i] = (AX[i] - s) / A[i, i]

        if (abs(x_new - x)/x_new).any() < tol:
            break

        x[:] = x_new
        num_iter += 1

    print('iteration = ',num_iter)
    return x


# Assist by ChatGPT
def Gauss_seidel(A, AX, tol=0.05, max_iter = 1000):
    """
    Solves a system of linear equations using the Gauss-Seidel iteration method.
    
    Args:
        A: a numpy array representing the coefficient matrix.
        AX: a numpy array representing the right-hand side vector.
        max_iter: an integer representing the maximum number of iterations.
        tol: a float representing the tolerance for convergence.
    
    Returns:
        x: a numpy array representing the solution vector.
    """
    n = len(A)
    x = np.zeros(n)
    for iter_count in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (AX[i] - s1 - s2) / A[i, i]
        if abs((x - x_old)/x).any() < tol:
            break
    
    print('iteration = ',iter_count)

    return x


# Written by Z,L,Lin
def Least_Square_Regression(X, Y):
    '''
    Arg:
        X (NDarray): x of target array. (NumPy array)
        Y (NDarray): y of target array. (NumPy array)

    Return:
        Coefficient (NDarray): coefficient of regression line. (NumPy array)
    '''
    n = len(X)  # Number of data points
    # Calculate the 1st order coefficient (slope) of the regression line
    a1 = (n * np.sum(X * Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X ** 2) - (np.sum(X)) ** 2)
    # Calculate the 0th order coefficient (intercept) of the regression line
    a0 = np.average(Y) - a1 * np.average(X)
    Coefficient = np.array([a0, a1])  # Combine the coefficients into a NumPy array
    return Coefficient  # Return the coefficient of the regression line as a NumPy array


def poly_regress(x, y, order):
    """
    This function is designed to calculate the coefficients of Polynomial Regression using Gaussian Elimination.
    You can specify the order of the polynomial regression to be calculated.
    """
    # Initialize the matrix A & AX
    A = np.zeros((order+1, order+1))  # A is a square matrix with dimensions (order+1) x (order+1)
    AX = np.zeros(order+1)  # AX is a 1D array of length (order+1)
    
    # Compute the elements of AX and A using loop
    for i in range(order+1):
        AX[i] = np.sum((x**i) * y)  # Compute the sum of (x^i * y) for each i and store it in AX[i]
        for j in range(order+1):
            A[i, j] = np.sum(x**(i+j))  # Compute the sum of (x^(i+j)) for each i, j and store it in A[i, j]

    # Call the Gaussian_Elimination function to solve the linear equations and get the coefficients of Polynomial Regression
    cXY = Gaussian_Elimination(A, AX)  # cXY is a 1D array of length (order+1) representing the coefficients of the polynomial regression
    return cXY  # Return the coefficients of the Polynomial Regression


# Written by Z,L,Lin
def Regression_Line(X, Coefficients):
    '''
    The function is used to compute the regression value of poly_regress.

    Arg: 
        X (float, NDarray): target value. (data type: float or numpy ndarray)
        Coefficients (array): Coefficients of regression line. (data type: array, typically a list or numpy ndarray)

    Return:
        RL (NDarray): the regressed value. (data type: numpy ndarray)
    '''
    n = len(Coefficients)  # Get the number of coefficients
    RL = 0  # Initialize the regressed value to 0
    for i in range(n):  # Loop through each coefficient
        RL += Coefficients[i] * X ** i  # Compute the contribution of each coefficient to the regressed value
    return RL  # Return the regressed value


def Slope_2D(x, y, ODE_func):
    Slope = ODE_func(x,y)
    return Slope


def Slope_3D(x, y, z, ODE_func):
    Slope = ODE_func(x,y,z)
    return Slope


def Solve_Euler(x, y_initial, ODE_func, h):
    '''
    Args:
        x: NDarray
        y_initial: A initial value of y
        ODE_func: the ode function want to solve
        h: the step between two x

    Returns:
        x, y: NDarray
    '''
    length = int((x[-1] - x[0]) // h + 1)
    x = np.linspace(1,19,int(18//h+1),dtype=float)
    y = np.zeros(length,dtype=float)
    y[0] = y_initial

    for i in range(length-1):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*Slope_2D(x[i], y[i], ODE_func)

    return x, y


def Solve_ModEuler(x, y_initial, ODE_func, h):
    '''
    Args:
        x: NDarray
        y_initial: A initial value of y
        ODE_func: the ode function want to solve
        h: the step between two x

    Returns:
        x, y: NDarray
    '''
    length = int((x[-1] - x[0]) // h + 1)
    x = np.linspace(1,19,int(18//h+1),dtype=float)
    y = np.zeros(length,dtype=float)
    y[0] = y_initial

    for i in range(length-1):
        x[i+1] = x[i] + h
        sp1 = Slope_2D(x[i], y[i], ODE_func)
        yEu = y[i] + sp1 * h
        sp2 = Slope_2D(x[i+1], yEu, ODE_func)
        y[i+1] = y[i] + h * (sp1 + sp2) / 2

    return x, y


def Solve_RK4(x, y_initial, ODE_func, h):
    '''
    Args:
        x: NDarray
        y_initial: A initial value of y
        ODE_func: the ode function want to solve
        h: the step between two x

    Returns:
        x, y: NDarray
    '''
    length = int((x[-1] - x[0]) // h + 1)
    x = np.linspace(1,19,int(18//h+1),dtype=float)
    y = np.zeros(length,dtype=float)
    y[0] = y_initial

    for i in range(length-1):
        x[i+1] = x[i] + h
        sp1 = Slope_2D(x[i], y[i], ODE_func)
        sp2 = Slope_2D(x[i] + 0.5*h, y[i] + 0.5*sp1*h, ODE_func)
        sp3 = Slope_2D(x[i] + 0.5*h, y[i] + 0.5*sp2*h, ODE_func)
        sp4 = Slope_2D(x[i] + h, y[i] + sp3*h, ODE_func)
        y[i+1] = y[i] + h * (sp1 + 2*sp2 + 2*sp3 + sp4) / 6

    return x, y


def ODE2_Euler(x, y_initial, z_initial, ODE_func1, ODE_func2, h):
    '''
    Args:
        x: NDarray
        y_initial: A initial value of y
        z_initial: A initial value of z
        ODE_func1, ODE_func2: the ode functions we want to solve
        h: the step between two x

    Returns:
        x, y, z: NDarray
    '''
    y = np.zeros(len(x),dtype=float)
    z = np.zeros(len(x),dtype=float)

    y[0] = y_initial
    z[0] = z_initial

    for i in range(len(x)-1):
        x[i+1] = (x[i] + h)
        y[i+1] = (y[i] + h*Slope_3D(x[i], y[i], z[i], ODE_func1))
        z[i+1] = (z[i] + h*Slope_3D(x[i], y[i], z[i], ODE_func2))

    return x, y, z


# Define function solving 2-ODEs system
def ODE2_RK4(x, y_initial, z_initial, ODE_func1, ODE_func2, h):
    '''
    Args:
        x: NDarray
        y_initial: A initial value of y
        z_initial: A initial value of z
        ODE_func1, ODE_func2: the ode functions we want to solve
        h: the step between two x

    Returns:
        x, y, z: NDarray
    '''
    y = np.zeros(len(x),dtype=float)
    z = np.zeros(len(x),dtype=float)

    y[0] = y_initial
    z[0] = z_initial

    for i in range(len(x)-1):
        x[i+1] = x[i] + h
        sp1 = Slope_3D(x[i], y[i], z[i], ODE_func1)
        sp12 = Slope_3D(x[i], y[i], z[i], ODE_func2)

        sp2 = Slope_3D(x[i] + 0.5*h, y[i] + 0.5*sp1*h, z[i] + 0.5*sp12*h, ODE_func1)
        sp22 = Slope_3D(x[i] + 0.5*h, y[i] + 0.5*sp1*h, z[i] + 0.5*sp12*h, ODE_func2)

        sp3 = Slope_3D(x[i] + 0.5*h, y[i] + 0.5*sp2*h, z[i] + 0.5*sp22*h, ODE_func1)
        sp32 = Slope_3D(x[i] + 0.5*h, y[i] + 0.5*sp2*h, z[i] + 0.5*sp22*h, ODE_func2)

        sp4 = Slope_3D(x[i] + h, y[i] + sp3*h, z[i] + sp32*h, ODE_func1)
        sp42 = Slope_3D(x[i] + h, y[i] + sp3*h, z[i] + sp32*h, ODE_func2)

        y[i+1] = y[i] + h * (sp1 + 2*sp2 + 2*sp3 + sp4) / 6
        z[i+1] = z[i] + h * (sp12 + 2*sp22 + 2*sp32 + sp42) / 6

    return x, y, z


def ODEs_Solve_RK4(ODE_funcs, p0, vars, h):
    '''
    Args:
        ODE_funcs: a List of ode functions we want to solve
        p0: a initial value of dependent variable
        vars: a List of initial value of variables
        h: the step between two x

    Returns:
        v4: a tuple of NDarrays
    '''
    n = len(vars) # number of variables
    p = p0 # initial values of dependent variables

    # initialize arrays with zeros
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    k3 = np.zeros(n)
    k4 = np.zeros(n)
    v1 = np.zeros(n)
    v2 = np.zeros(n)
    v3 = np.zeros(n)
    v4 = np.zeros(n)

    for i in range(n):  # calculate k1 and v1 for each dependent variable
        k1[i] = ODE_funcs[i](p, *vars) 
        v1[i] = vars[i] + k1[i] * h / 2 

    p = p0 + h / 2  # update the value of the independent variable
    for i in range(n): 
        k2[i] = ODE_funcs[i](p, *v1) 
        v2[i] = vars[i] + k2[i] * h / 2 

    p = p0 + h / 2
    for i in range(n):
        k3[i] = ODE_funcs[i](p, *v2)
        v3[i] = vars[i] + k3[i] * h

    p = p0 + h
    for i in range(n):
        k4[i] = ODE_funcs[i](p, *v3)
        v4[i] = vars[i] + (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) * h / 6  # calculate the final value of the ith dependent variable using the weighted average of k1, k2, k3, and k4

    return tuple(v4)  # return the final values of the dependent variables as a tuple


def trapezoidal_method(a, b, n, func):
    '''
    Args:
        a: lower limit
        b: upper limit
        n: how many slice
        func: the function we want to apply integral
    
    Returns:
        integral: value of integration
    '''
    h = ((b - a) / n)
    sum_val = 0
    for i in range(1, n):
        x = a + i * h
        sum_val += func(x)
    integral = h / 2 * (func(a) + func(b) + 2 * sum_val)
    return integral


def simpsons_one_third(a, b, n, func):
    '''
    Args:
        a: lower limit
        b: upper limit
        n: how many slice
        func: the function we want to apply integral
    
    Returns:
        integral: value of integration
    '''
    h = ((b - a) / n)
    sum_val1 = 0
    sum_val2 = 0

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            sum_val2 += func(x)
        else:
            sum_val1 += func(x)

    integral = h / 3 * (func(a) + func(b) + 4 * sum_val1 + 2 * sum_val2)
    return integral


