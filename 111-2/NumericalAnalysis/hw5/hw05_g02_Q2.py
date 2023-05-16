import numpy as np
import matplotlib.pyplot as plt
import time

# Define functions
def Jacobi_iteration(A, AX, x0=None, tol = 0.05, max_iter=1000):
    """
    Solves the system of linear equations A * x = AX using Jacobi iteration method.

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
def Gaussian_Elimination(A, AX):  # Assist by ChatGPT
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

# Read data
z, t_ini = np.loadtxt(fname='T_ini.txt',dtype=float,skiprows=1,delimiter=',',unpack=True)
t, t_s = np.loadtxt(fname='T_s.txt',dtype=float,skiprows=1,delimiter=',',unpack=True)

# Define Array A
M = 5e-7 * 10000   # [m^2/s]
A = np.zeros((20,20),dtype=float)
for i in range(19):
    A[i,i] = 1 + 2*M
    A[i+1,i] = -M
    A[i,i+1] = -M
A[19,19] = 1 + M

# Define iterated temp. throught time (time,Temp.) = (1440,20)
t_n = np.zeros((len(t_s),len(t_ini)),dtype=float)
for i in range(0,len(t_ini)):
    t_n[0][i] = t_ini[i]

# Solve the equation system using different method
start = time.time()
for i in range(0,len(t)-1):
    t_n[i,0] += M * t_s[i] 
    t_n[i+1][:] = Gaussian_Elimination(A,t_n[i][:])
end = time.time()

# Plot the iterated outcome
t_transpose = t_n.transpose()
for i in range(0,len(t_ini)):
    plt.plot(t,t_transpose[i][:])
plt.xlim(0,1438)
plt.title('Diurnal Cycle of Soil Temp.')
plt.xlabel('time [min]')
plt.xticks(np.linspace(0,24*60,25))
plt.ylabel('Soil Temp. [\u2103]')
plt.show()
plt.savefig('Jacobi.png')

# Calculate processing time
print('process time =',end - start, ' [s]')