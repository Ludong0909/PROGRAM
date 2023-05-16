import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,10)
y = 1 + np.exp(-x/5)*np.sin(2*x)

ys_ind = np.argsort(y)
ys_indr = ys_ind[::-1]

f,ax=plt.subplots(2,2,sharex='all')
ax[0,0].plot(x,y,'b-o')
ax[0,1].plot(x,y[ys_indr],'bo')
ax[1,0].plot(x,ys_indr,'bo')
ax[1,1].plot(x[ys_ind],y[ys_ind],'b-o')

plt.show()
