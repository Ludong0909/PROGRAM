import numpy as np
import matplotlib.pyplot as plt
from time import process_time


class GSIter():
    def __init__(self, A, AX):
        self.n = len(AX)
        if (np.shape(A) != (self.n, self.n)):
            raise ValueError("A or AX is wrong!")
        self.A = A
        self.AX = AX
        self.X = np.zeros((1,self.n))
        self.i = 0

    def iterate(self):
        self.i += 1
        self.X = np.append(self.X, np.zeros((1,self.n)), axis=0)
        #self.X[self.i][0] = 1/self.A[0][0] * (self.AX[0] - (np.dot(self.A[0][1:], self.X[self.i-1][1:])))
        for i in range(self.n):
            self.X[self.i][i] = 1/self.A[i][i] * (self.AX[i] - (np.dot(self.A[i][0:i],self.X[self.i][0:i]) + np.dot(self.A[i][i+1:],self.X[self.i-1][i+1:])))
        #print("GS")
    
    def IterateTimes(self):
        return "Iterated %i times"%(self.i)

class JcIter():
    def __init__(self, A, AX, X=None):
        self.n = len(AX)
        if (np.shape(A) != (self.n, self.n)):
            raise ValueError("A or AX is wrong!")
        self.A = A
        self.AX = AX
        if X == None:
            self.X = np.zeros((1,self.n))
        else:
            self.X = X
        self.i = 0

    def iterate(self):
        self.i += 1
        self.X = np.append(self.X, np.zeros((1,self.n)),axis=0)
        for i in range(self.n):
            self.X[self.i][i] = 1/self.A[i][i] * (self.AX[i] - (np.dot(self.A[i][0:i],self.X[self.i-1][0:i]) + np.dot(self.A[i][i+1:],self.X[self.i-1][i+1:])))
    
    def IterateTimes(self):
        return "Iterated %i times"%(self.i)

e = 0.05

A1 = np.array([[9, -2, 3, 2],
               [2, 8, -2, 3],
               [-3, 2, 11, -4],
               [-2, 3, 2, 10]])
AX1 = np.array([54.5, -14, 12.5, -21])

N1GS = GSIter(A1, AX1)
start1 = process_time()
N1GS.iterate()
N1GS.iterate()
while ((np.abs((N1GS.X[-1]-N1GS.X[-2])/N1GS.X[-2]) >= e).any()):
    N1GS.iterate()
end1 = process_time()
print(N1GS.X[-1])
print(N1GS.IterateTimes(), "time used: %f sec"%(end1-start1))

N1J = JcIter(A1,AX1)
start2 = process_time()
N1J.iterate()
N1J.iterate()
while ((np.abs((N1J.X[-1]-N1J.X[-2])/N1J.X[-2]) >= e).any()):
    N1J.iterate()
end2 = process_time()
print(N1J.X[-1])
print(N1J.IterateTimes(), "time used: %f sec"%(end2-start2))

Color = ("#1f77b4","#ff7f0e","#2ca02c","#d62728")
f1, ax1 = plt.subplots(2,1,sharex="all")

for i in range(N1GS.n):
    ax1[0].plot(np.linspace(0,N1GS.i,N1GS.i+1),N1GS.X[:,i],color=Color[i])
    ax1[0].text(N1GS.i+0.05,N1GS.X[N1GS.i,i]-0.3,"X%i"%(i+1),color=Color[i])

for i in range(N1J.n):
    ax1[1].plot(np.linspace(0,N1J.i,N1J.i+1),N1J.X[:,i],color=Color[i])
    ax1[1].text(N1J.i+0.05,N1J.X[N1J.i,i]-0.3,"X%i"%(i+1),color=Color[i])

f1.suptitle("The Evolution of $(X_1,X_2,X_3,X_4)$ in each Iteration Step")
ax1[1].set_xlabel("Iterations (times)")
ax1[0].set_title("Gauss-Seidel Iterative Method")
ax1[1].set_title("Jacobi Iterative Method")

f1.savefig("hw5q1.png", dpi=500)
plt.show()