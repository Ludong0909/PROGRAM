import numpy as np
import Cheers

A = np.array([[9,-2,3,2],[2,8,-2,3],[-3,2,11,-4],[-2,3,2,10]],dtype=float)
AX = np.array([54.5,-14,12.5,-21])

Jacobi = Cheers.Jacobi_iteration(A,AX,tol=0.05)
GS = Cheers.Gauss_seidel(A,AX,tol=0.05)

print(Jacobi)
print(GS)

