import numpy as np

# Define Method
def GaussElimination(A,AX):
    '''
    recieve A: target array
            AX : answer array of equation system
    '''
    n = len(AX)

    # Sort the equations 
    Aindex = np.argsort(np.abs(np.transpose(A)[:][0]))
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

# Q3.1---------------------------------------
A = np.array([[0,2,3],[4,-3,2],[2,4,-3]],dtype=float)
AX = np.array([46,16,12],dtype=float)
A,AX = GaussElimination(A,AX)
X = BackwardSub(A,AX)
print(X)


# Q3.2---------------------------------------
B = np.array([[1,2,3,4,5],[2,4,4,-2,1],[3,-4,1,-1,3],[4,1,2,2,3],[5,5,-3,1,4]],dtype=float)
BX = np.array([23,30,30,23,3],dtype=float)

B,BX = GaussElimination(B,BX)
XB = BackwardSub(B,BX)
print(XB)
