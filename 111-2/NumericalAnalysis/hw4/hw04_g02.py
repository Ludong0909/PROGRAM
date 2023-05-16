import numpy as np

# 1.1
def BackwardSub(A, AX):
    n = len(AX)
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = (AX[i]-np.dot(A[i][:], X))/A[i][i]
    return X

# 1.2
A1 = np.array([[1, 2, 2     , 1     ],
               [0,-8,-3     ,-7     ],
               [0, 0,-4.8750,-3.3750],
               [0, 0, 0     ,-5.5385]],dtype=float)
AX1 = np.array([17,-26,-14.25,16.6155],dtype=float)
X1 = BackwardSub(A1,AX1)
print("# 1.2",X1)

# 1.3
A2 = np.array([[1, 2, 3,  4, 5],
               [0,-7,-2,-10, 9],
               [0, 0, 1,  5, 4],
               [0, 0, 0,  2, 4],
               [0, 0, 0,  0, 2]],dtype=float)
AX2 = np.array([23,63,6,10,8],dtype=float)
X2 = BackwardSub(A2, AX2)
print("# 1.3",X2)

# 2.1
def Gauss_elim(A, AX):
    n = len(AX)
    for i in range(n):
        for j in range(i+1,n):
            AX[j] = AX[j] - AX[i]*(A[j][i]/A[i][i])
            A[j] = A[j] - A[i]*(A[j][i]/A[i][i])
    X = BackwardSub(A,AX)
    return X

# 2.2
A3 = np.array([[ 1, 2, 2, 1],
               [ 2,-4, 1,-5],
               [ 2, 1,-2,-4],
               [-1, 2, 1,-2]],dtype=float)
AX3 = np.array([17, 8,10,17],dtype=float)
X3 = Gauss_elim(A3,AX3)
print("# 2.2",X3)

# 2.3
A4 = np.array([[ 1, 2, 3, 4, 5],
               [ 2,-3, 4,-2, 1],
               [ 3,-4, 1,-1, 3],
               [ 4, 1, 2, 2, 3],
               [ 5, 5,-3, 1, 4]],dtype=float)
AX4 = np.array([23,37,30,23, 3],dtype=float)
X4 = Gauss_elim(A4,AX4)
print("# 2.3",X4)


def PartialPivot(A, AX, i):
    """Performs partial pivoting on the matrix A and the vector AX"""
    n = A.shape[0]
    max_index = i
    for j in range(i+1, n):
        if abs(A[j, i]) > abs(A[max_index, i]):
            max_index = j
    if max_index != i:
        A[[i, max_index]] = A[[max_index, i]]
        AX[[i, max_index]] = AX[[max_index, i]]
    return A, AX

def Gauss_elim(A, AX):
    n = len(AX)
    for i in range(n):
        A, AX = PartialPivot(A, AX, i)
        for j in range(i+1,n):
            AX[j] = AX[j] - AX[i]*(A[j][i]/A[i][i])
            A[j] = A[j] - A[i]*(A[j][i]/A[i][i])
    X = BackwardSub(A,AX)
    return X

# 3.1
A5 = np.array([[ 0, 2, 3],
               [ 4,-3, 2],
               [ 2, 4,-3]],dtype=float)
AX5 = np.array([46,16,12],dtype=float)
X5 = Gauss_elim(A5,AX5)
print("# 3.1",X5)

# 3.2
A6 = np.array([[ 1, 2, 3, 4, 5],
               [ 2, 4, 4,-2, 1],
               [ 3,-4, 1,-1, 3],
               [ 4, 1, 2, 2, 3],
               [ 5, 5,-3, 1, 4]],dtype=float)
AX6 = np.array([23,30,30,23, 3],dtype=float)
X6 = Gauss_elim(A6,AX6)
print("# 3.2",X6)
