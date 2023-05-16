import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

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

T0 = np.array([3,6,9,12,15,18,21,24],dtype=np.float64)
Ts0 = np.array([2.1,3.0,2.1,0,-2.1,-3,-2.1,0],dtype=np.float64)

linear = interpolate.interp1d(T0,Ts0,kind="linear",fill_value="extrapolate") # type: ignore
cubic = interpolate.interp1d(T0,Ts0,kind="cubic",fill_value="extrapolate") # type: ignore
nearest = interpolate.interp1d(T0,Ts0,kind="nearest",fill_value="extrapolate") # type: ignore

T = np.linspace(1,24,24)
Ts_linear = linear(T)
Ts_cubic = cubic(T)
Ts_nearest = nearest(T)

cTs7 = poly_regress(T0,Ts0,7)
RLTs7 = RegressionLine(T,cTs7)

plt.plot(T,Ts_linear,'o-',markersize = '5', alpha = 0.8)
plt.plot(T,Ts_cubic,'o-',markersize = '5', alpha = 0.8)
plt.plot(T,Ts_nearest,'o-',markersize = '5', alpha = 0.8)
plt.plot(T,RLTs7,'o-',color = 'pink',markersize = '5', alpha = 1)
plt.plot(T0,Ts0,"o",alpha = 1)
plt.legend(['linear','cubic','nearest','7th-order','Ts'])
plt.title('Surface Temp.')
plt.xlabel('hour')
plt.ylabel('Temp. [\u2103]')
plt.savefig("hw06_g02_3.png",dpi=500)
plt.show()