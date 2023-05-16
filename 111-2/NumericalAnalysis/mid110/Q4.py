import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

X = np.linspace(0,6,16,dtype=float)
Y = np.array([0.0, 3.0, 4.5, 5.8, 5.9, 5.8, 6.2, 7.4, 9.6, 15.6, 20.7, 26.7, 31.1, 35.6, 39.3, 41.5],dtype=float)

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

cXY = poly_regress(X,Y,5)
RL = Regression_Line(X,cXY)

plt.plot(X,Y,'o')
plt.plot(X,RL)
plt.grid()
plt.show()

