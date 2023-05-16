import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100000)
y = 1 + np.exp(-x/5)*np.sin(2*x)

print(np.amax(y))
print(np.argmax(y))
print(x[np.argmax(y)])

plt.plot(x,y,'b-')
plt.plot(x[np.argmax(y)],y[np.argmax(y)],'r*')
plt.show()

