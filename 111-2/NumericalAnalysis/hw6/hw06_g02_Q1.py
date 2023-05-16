import numpy as np
import matplotlib.pyplot as plt

# Q1.1
T = np.array([0,10,20,30,40,50,60,70,80,90,100],dtype=float)
P = np.array([0.94,0.96,1,1.05,1.07,1.09,1.14,1.17,1.21,1.24,1.28])

def linear_least_squares_regression(T, P):
    # Convert the input lists to numpy arrays
    T = np.array(T)
    P = np.array(P)
    
    # Calculate the number of data points
    n = len(T)
    
    # Calculate the necessary sums for the regression equations
    sum_T = np.sum(T)
    sum_P = np.sum(P)
    sum_T_squared = np.sum(T**2)
    sum_TP = np.sum(T*P)
    
    # Calculate the coefficients "a" and "b"
    slope = (n*sum_TP - sum_T*sum_P) / (n*sum_T_squared - sum_T**2)
    intercept = (sum_P - slope*sum_T) / n
    regression_array = T * slope + intercept

    return slope, intercept, regression_array

'''
slope, intercept, regression = linear_least_squares_regression(T,P)
print(slope,intercept)

plt.plot(T,regression,'o-')
plt.plot(T,P,'o')
plt.grid()
plt.xlabel('T')
plt.ylabel('P')
plt.legend(['Regression Line: P = 0.0342T+0.9336','P'])
plt.title('Regression Line of P v.s. T')
plt.show()
'''
# Q1.2
Ts = np.loadtxt(fname='Ts_1901_2013_global_average.txt',dtype=float,skiprows=0,delimiter=',',unpack=True)
print(len(Ts))
x = np.linspace(1901,2013,113)
a,b,RL = linear_least_squares_regression(x,Ts)

for i in range(len(Ts)//10-1):
    a,b,array = linear_least_squares_regression(x[10*i:10*i+10],Ts[10*i:10*i+10])
    plt.plot(x[10*i:10*i+10],array)

a,b,RL13 = linear_least_squares_regression(x[100:113],Ts[100:113])
plt.plot(x[100:113],RL13)
plt.plot(x,RL)
plt.plot(x,Ts,'o',alpha = 0.3)
plt.grid()
plt.show()

