import numpy as np
import matplotlib.pyplot as plt

'''
import the given arrays
'''
T = np.array([0,10,20,30,40,50,60,70,80,90,100],dtype=np.float64)
P = np.array([0.94,0.96,1.0,1.05,1.07,1.09,1.14,1.17,1.21,1.24,1.28],dtype=np.float64)

'''
P = a*T+b
'''
'''
Least Squares Regression
'''
def LeastSquareRegression(X,Y):
    n = len(X)
    # 1st order coefficient
    a1 = (n * np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-(np.sum(X))**2)
    # 0st order coefficient
    a0 = np.average(Y)-a1*np.average(X)
    cs = np.array([a0,a1])
    return cs

def RegressionLine(X,cs):
    n = len(cs)
    RL = 0
    for i in range(n):
        RL += cs[i]*X**i
    return RL

csTP = LeastSquareRegression(T,P)
RLTP = RegressionLine(T,csTP)
print(csTP)

plt.plot(T,RLTP)
plt.plot(T,P,"o")
plt.legend()
plt.show()


