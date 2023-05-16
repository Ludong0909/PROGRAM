import numpy as np
import matplotlib.pyplot as plt

dt=1.
x0=10.
tf=10+1

t=np.arange(0,tf,dt)
x=np.zeros(tf)
#v=0.4*t**3-2*t+9

x[0]=x0

for i in range(1,tf): #range cant not be float
    v=0.4*i**3-2*i+9
    x[i]=x[i-1]+v*dt

plt.plot(t,x,'b-')
plt.show()
