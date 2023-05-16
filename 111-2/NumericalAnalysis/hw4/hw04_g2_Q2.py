import numpy as np

# Define Method
def GaussElimination(A,AX):
    '''
    recieve A: target array
            AX : answer array of equation system
    '''
    n = len(AX)

    # Sort the eqsations 
    Aindex = np.argsort(np.transpose(A)[:][0])
    Asort = np.zeros(np.shape(A))
    AXsort = np.zeros(np.shape(AX))
    for i in range(len(Aindex)):
        Asort[:][i] = A[:][Aindex[i]]
        AXsort[i] = AX[Aindex[i]]
    A = np.flip(Asort,axis=0)
    AX = np.flip(AXsort)

    # Gauss Elimination
    for j in range(n-1):
        for i in range(j+1,n):
            AX[i] = AX[i] - AX[j] * (A[i][j]) / A[j][j]
            A[i][j:n] = A[i][j:n] - A[j][j:n] * (A[i][j]/A[j][j])

    return(A,AX)

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

# Q2.2----------------------------
A = np.array([[1,2,2,1],[2,-4,1,-5],[2,1,-2,-4],[-1,2,1,-2]],dtype=float)
AX = (np.array([17,8,10,17],dtype=float))

A,AX = GaussElimination(A,AX)
X = BackwardSub(A,AX)
print(X)

# Q2.3----------------------------
B = np.array([[1,2,3,4,5],[2,-3,4,-2,1],[3,-4,1,-1,3],[4,1,2,2,3],[5,5,-3,1,4]],dtype=float)
BX = np.array([23,37,30,23,3],dtype=float)

B,BX = GaussElimination(B,BX)
BX = BackwardSub(B,BX)
print(BX)