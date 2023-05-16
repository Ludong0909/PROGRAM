import numpy as np
import myfunc 

P,T,Q=np.loadtxt('P_T_Q2.txt',skiprows=1,unpack=True)
Es=myfunc.Esat(T)
print(Es)


