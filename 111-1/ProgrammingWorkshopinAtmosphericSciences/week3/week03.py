import numpy as np
import matplotlib.pyplot as plt



nmax=20+1
x = np.zeros(nmax)
x[0]=0
x[1]=1
for n in range(2,nmax) :
    x[n]=x[n-1]+x[n-2]
        

plt.plot(np.arange(nmax),x,'bd')
plt.show()