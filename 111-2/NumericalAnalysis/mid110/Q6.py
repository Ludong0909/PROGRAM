import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def Gauss_seidel(A, AX, tol=0.05, max_iter = 100000, weight = 0.5):
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
            x[i] = weight * ((AX[i] - s1 - s2) / A[i, i]) + (1 - weight) * x_old[i]
        if abs((x - x_old)/x).any() < tol:
            break
    
    print('iteration = ',iter_count)

    return x

A = np.array([[9,-2,3,2],[2,8,-2,3],[-3,2,11,-4],[-2,3,2,10]],dtype=float)
AX = np.array([54.5,-14,12.5,-21])

x = Gauss_seidel(A,AX,tol=0.001,weight=0.9)
print(x)