'''
module: NAFunc
'''
import numpy as np

''' Description
# This function brackets the root of a given function f
# within the interval (x1,x2) using the bisection method 
# with zero as the target value of the function
# Inputs:
# f : function whose root is to be found
# target : target value of the function (zero by default)
# x1 : lower bound of the interval
# x2 : upper bound of the interval
# Tolerance : tolerance level for the root
# Returns: midpoint of the final bracketing interval
'''
# Bad
def BracketRoot0(f, target=0, x1=0, x2=1, Tolerance=1e-6):
    import numpy as np
    InitialSection = abs(x2-x1)
    # check if the interval contains a root
    if ((f(x1)*f(x2))<0):
        # iterate until tolerance level is reached
        for i in range(round(np.log(InitialSection/Tolerance)/np.log(2))):
            # calculate midpoint of the interval
            x3 = (x1+x2)/2
            if ((f(x1)*f(x3)) < 0):
                x2 = x3
            elif ((f(x1)*f(x3)) > 0):
                x1 = x3
            else:
                # root found at midpoint
                if (f(x1) == 0):
                    return x1
                elif (f(x2) == 0):
                    return x2
                else:
                    print("error")
                    return 0
        return (x1+x2)/2
    # check if the endpoints themselves are roots
    elif (f(x1) == 0):
        return x1
    elif (f(x2) == 0):
        return x2
    else:
        print("Invalid input")
        return 0
    
''' Description
# This function brackets the root of a given function f
# within the interval (x1,x2) using the bisection method 
# with zero as the target value of the function
# Inputs:
# f : function whose root is to be found
# target : target value of the function (zero by default)
# x1 : lower bound of the interval
# x2 : upper bound of the interval
# Tolerance : tolerance level for the root
# Returns: midpoint of the final bracketing interval
'''

# Fund root by Bisection Method
def BisectionRoot(f, target=0, x1=0., x2=1., Tolerance=1e-6):
    iterateTime = 0
    # check if the interval is valid and contains a root
    if ((x1<x2) and (f(x1)*f(x2))<0):
        iterateTime += 1
        # iterate until tolerance level is reached
        while ((x2-x1) >= Tolerance):
            # calculate midpoint of the interval
            x3 = (x1+x2)/2
            if ((f(x1)*f(x3)) < 0):
                x2 = x3
            elif ((f(x1)*f(x3)) > 0):
                x1 = x3
            elif (f(x3) == 0):
                print("Iterate %i times"%iterateTime)
                return x3
            else:
                print("Some error occured")
                return 0
        print("Iterate %i times"%iterateTime)
        return (x1+x2)/2
    # check if the endpoints themselves are roots
    elif (f(x1) == 0):
        print("Iterate %i times"%iterateTime)
        return x1
    elif (f(x2) == 0):
        print("Iterate %i times"%iterateTime)
        return x2
    else:
        print("Invalid input: x1 and x2 are in the same sign")
        return 0

# Bad
def NewtonRoot0 (f, target=0, x1=1, Tolerance=1e-6):
    df = np.gradient(f)
    x2 = 0
    while abs(x2-x1) > Tolerance:
        x2 = x1-f(x1)/df(x1)
    return x2

# define a function to find root using the Newton-Raphson method
def NewtonRoot (f, df, x1=1, Tolerance=1e-6):
    # initialize counter
    i = 1
    
    # calculate the first iteration
    x2 = x1-f(x1)/df(x1)
    # print current iteration and the new value of x
    print("    Finding Newton Root #%i, currently at" %i, x2)
    
    # iterate until the tolerance level is reached
    while (abs(x2-x1) > Tolerance):
        x1 = x2
        x2 = x1-f(x1)/df(x1)
        i += 1
        # print current iteration and the new value of x
        print("    Finding Newton Root #%i, currently at"%i, x2)
    
    return x2

# Find Root by Secant Method
def SecRoot (f, x0, x1, TOL=1e-6):
    while abs(x0-x1) > TOL:
        x2 = x1-f(x1)*(x0-x1)/(f(x0)-f(x1))
        x0 = x1
        x1 = x2
    return (x0+x1)/2

# Something cool
def get_matrix_input(rows=3, columns=3):
    import tkinter as tk
    root = tk.Tk()

    # Create a matrix of input fields
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            entry = tk.Entry(root, width=5)
            entry.grid(row=i, column=j)
            row.append(entry)
        matrix.append(row)

    # Create a button to submit the matrix values
    def submit_matrix():
        values = []
        for row in matrix:
            row_values = []
            for entry in row:
                row_values.append(int(entry.get()))
            values.append(row_values)
        matrix_array = np.array(values)
        root.destroy()
        return matrix_array

    submit_button = tk.Button(root, text="Submit", command=submit_matrix)
    submit_button.grid(row=3, column=1)

    root.mainloop()

def BackwardSub(A, AX):
    n = len(AX)
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = (AX[i]-np.dot(A[i][:], X))/A[i][i]
    return X

# I don't know if this even work, and the new Gauss Elimination doesn't use this
def Check0(A,AX,i):
    if (A[i][i] == 0):
        index = np.argsort(A[i:][i], axis=0)
        A[i:] = A[index]
        AX[i:] = AX[index]
        return A,AX

# Bad
def GaussElimination0(A, AX):
    n = len(AX)
    for i in range(n):
        A,AX = Check0(A,AX,i)  # type: ignore
        for j in range(i+1,n):
            A[j] = A[j] - A[i]*(A[j][i]/A[i][i])
            AX[j] = AX[j] - AX[i]*(A[j][i]/A[i][i])
    X = BackwardSub(A,AX)
    return X

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

class GJIter():
    def __init__(self, A, AX):
        self.n = len(AX)
        if (np.shape(A) != (self.n, self.n)):
            raise ValueError("A or AX is wrong!")
        self.A = A
        self.AX = AX
        self.X = np.zeros((1,self.n))
        self.i = 0

    def BackwardSub(self, A, AX):
        for i in range(self.n-1, -1, -1):
            self.X[self.i] = (AX[i]-np.dot(A[i][:], self.X[self.i]))/A[i][i]

    def GaussElimination(self):
        self.i += 1
        self.X = np.append(self.X, np.zeros((1,self.n)), axis=0)
        A = self.A
        AX = self.AX
        for i in range(self.n):
            #A,AX = Check0(A,AX,i)  # type: ignore
            for j in range(i+1,self.n):
                A[j] = self.A[j] - self.A[i]*(self.A[j][i]/self.A[i][i])
                self.AX[j] = self.AX[j] - self.AX[i]*(self.A[j][i]/self.A[i][i])
        self.BackwardSub(A,AX)

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

# Gauss Seidel Iteration
def Gauss_Seidel_Iteration(A,AX,preX,n):
    X = np.zeros(n)
    for j in range(n):
        X[j] = 1/A[j][j] * (AX[j] - (np.dot(A[j][0:j],X[0:j]) + np.dot(A[j][j+1:],preX[j+1:])))
    return X

# Jocobi Iteration
def Jacobi_Iteration(A,AX,preX,n):
    X = np.zeros(n)
    for j in range(n):
        X[j] = 1/A[j][j] * (AX[j] - (np.dot(A[j][0:j],preX[0:j]) + np.dot(A[j][j+1:],preX[j+1:])))
    return X

# Linear Regression by Least Square Method
def LeastSquareRegression(X,Y):
    n = len(X)
    # 1st order coefficient
    a1 = (n * np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-(np.sum(X))**2)
    # 0st order coefficient
    a0 = np.average(Y)-a1*np.average(X)
    Coeffecient = np.array([a0,a1])
    return Coeffecient

# Polynomial Regression
def Poly_Regression(X,Y,n):
    n = n+1
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            A[i][j] = np.sum(X**(i+j))
    #A[0][0] = len(X)
    AX = np.zeros(n)
    for i in range(n):
        AX[i] = np.sum((X**i)*Y) 
    cXY = GaussElimination(A,AX)
    return cXY

# Draw the regression line by regressed coefficients
def RegressionLine(X,Coefficients):
    n = len(Coefficients)
    RL = 0
    for i in range(n):
        RL += Coefficients[i]*X**i
    return RL