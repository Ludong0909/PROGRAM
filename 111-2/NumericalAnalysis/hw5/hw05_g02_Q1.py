import numpy as np
import Cheers
import time

A = np.array([[9,-2,3,2],[2,8,-2,3],[-3,2,11,-4],[-2,3,2,10]],dtype=float)  # input matrix
AX = np.array([54.5,-14,12.5,-21],dtype=float)  # answer of input matrix
n = len(A[0][:])  # size of input array

X = np.array([2,5,6,9],dtype=float)  # X for innitial value

epsilon = np.ones(n) * 0.05  # criteria

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

start = time.time()
ans = Jacobi_iteration(A,AX)
end = time.time()

start1 = time.time()
ans1 = Gauss_seidel(A,AX)
end1 = time.time()

start2 = time.time()
ans2 = Cheers.Gaussian_Elimination(A,AX)
end2 = time.time()

print(ans)
print('Jacobi processing time =',end - start)
print(ans1)
print('Gauss-Seidel processing time =',end1 - start1)
print(ans2)
print('Gauss-Elim. processing time =',end2 - start2)
