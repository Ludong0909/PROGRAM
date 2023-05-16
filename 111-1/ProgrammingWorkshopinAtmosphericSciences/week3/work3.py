import numpy as np
import matplotlib.pyplot as plt

A=np.loadtxt('A.txt')
print(A)
AT=np.transpose(A)
print(AT)

B=np.log10(AT)
print(B)

out=np.column_stack((AT[:,0],B[:,0],AT[:,1],B[:,1],AT[:,2],B[:,2]))

print(out)

np.savetxt('AtB.txt',out,fmt='%5.2f',header='A0     logA0     A1     logA1     A2     logA2')