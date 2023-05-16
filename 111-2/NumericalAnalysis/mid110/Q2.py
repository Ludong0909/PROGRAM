import numpy as np
import sympy as sym

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

h = np.array([1,4000,8000,12000,16000,20000],dtype=float)
rho = np.array([1.225,0.820,0.525,0.309,0.168,0.092],dtype=float)

ln_rho = np.log(rho)

cXY = Least_Square_Regression(h, ln_rho)
print(cXY)

rho_7000 = np.exp(cXY[0]+ 7000*cXY[1])

print(rho_7000)