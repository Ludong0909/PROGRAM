import numpy as np
import matplotlib.pyplot as plt

'''
import the arrays
'''
Ts = np.loadtxt("Ts_1901_2013_global_average.txt",dtype=np.float64)
Year = np.linspace(1901,2013,113)

def LeastSquareRegression(X,Y):
    n = len(X)
    # 1st order coefficient
    a1 = (n * np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-(np.sum(X))**2)
    # 0st order coefficient
    a0 = np.average(Y)-a1*np.average(X)
    Coeffecient = np.array([a0,a1])
    return Coeffecient

def RegressionLine(X,cs):
    n = len(cs)
    RL = 0
    for i in range(n):
        RL += cs[i]*X**i
    return RL

cAll = LeastSquareRegression(Year,Ts)
RLAll = RegressionLine(Year,cAll)

plt.plot(Year,RLAll)
plt.plot(Year,Ts,"b.",alpha=0.3)

for i in range(10):
    c10 = LeastSquareRegression(Year[10*i:10*i+10],Ts[10*i:10*i+10])
    RL10 = RegressionLine(Year[10*i:10*i+10],c10)
    #plt.plot(Year[10*i:10*i+10],RL10)
c13 = LeastSquareRegression(Year[100:113],Ts[100:113])
RL13 = RegressionLine(Year[100:113],c13)
#plt.plot(Year[100:113],RL13)
plt.xlabel('year')
plt.ylabel('Avg. Temp. [\u2103]')
plt.title('Yearly Global Surface Temp.')
plt.savefig('YGST.png',dpi = 500)
plt.show()
