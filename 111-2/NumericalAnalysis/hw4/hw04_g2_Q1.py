import numpy as np

# Define Method
def BackwardSub(A,AX):
    '''
    recieve A: target array
            AX: the answer of equation system
    '''
    n = len(AX)
    X = AX

    for i in range(n):
        for j in range(i):
            X[n-i-1] = X[n-i-1] - A[n-i-1][n-i+j] * X[n-i+j]
        X[n-i-1] = X[n-i-1]/A[n-i-1][n-i-1]

    return X

# Q1.2--------------------------------------------------------------
A = np.array([[1,2,2,1],[0,-8,-3,-7],[0,0,-4.8750,-3.3750],[0,0,0,-5.5385]],dtype=float)
AX = np.array([17,-26,-14.25,16.6155],dtype=float)

X = BackwardSub(A,AX)

print(X)

# Q1.3--------------------------------------------------------------
B = ([1,2,3,4,5],[0,-7,-2,-10,9],[0,0,1,5,4],[0,0,0,2,4],[0,0,0,0,2])
BX = ([23,63,6,10,8])

XB = BackwardSub(B,BX)

print(XB)