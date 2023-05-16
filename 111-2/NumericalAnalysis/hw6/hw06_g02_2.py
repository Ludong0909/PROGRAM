import numpy as np
import matplotlib.pyplot as plt
import Cheers

def LeastSquareRegression(X,Y):
    n = len(X)
    # 1st order coefficient
    a1 = (n * np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-(np.sum(X))**2)
    # 0st order coefficient
    a0 = np.average(Y)-a1*np.average(X)
    Coeffecient = np.array([a0,a1])
    return Coeffecient

def GaussElimination(A, AX):  # Assist by ChatGPT
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
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        X[i] = (M[i, -1] - np.dot(M[i, :-1], X)) / M[i, i]
    return X

def poly_regress(X,Y,n):
    n = n+1
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            A[i][j] = np.sum(X**(i+j))
#    A = np.array(np.sum([[X**(i+j) for i in range(n)] for j in range(n)]))
    A[0][0] = n
#    AX = np.array(np.sum((X**i)*Y) for i in range(n))
    AX = np.zeros(n)
    for i in range(n):
        AX[i] = np.sum((X**i)*Y) 
    cXY = GaussElimination(A,AX)
    return cXY

def RegressionLine(X,Coefficients):
    n = len(Coefficients)
    RL = 0
    for i in range(n):
        RL += Coefficients[i]*X**i
    return RL

X = np.array([0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6,4.0,4.4,4.8,5.2,5.6,6.0],dtype=np.float64)
Y = np.array([0,3,4.5,5.8,5.9,5.8,6.2,7.4,9.6,15.6,20.7,26.7,31.1,35.6,39.3,41.5],dtype=np.float64)

cXY4 = poly_regress(X,Y,4)
cXY5 = Cheers.poly_regress(X, Y, 5)
RLXY4 = RegressionLine(X,cXY5)

print(cXY4)
plt.plot(X,RLXY4)
plt.plot(X,Y,"b.",alpha=0.3)
plt.show()
