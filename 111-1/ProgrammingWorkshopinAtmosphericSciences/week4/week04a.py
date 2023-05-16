import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,10)
y = 1 + np.exp(-x/5)*np.sin(2*x)
plt.plot(x,y,'b-')
plt.plot(x[(y<1.0)],y[(y<1.0)],'r*')
plt.plot(x[((x>5.0)*(y<1.0))],y[((x>5.0)*(y<1.0))],'b^')
plt.plot(x[((x>5.0)+(y<1.0))],y[((x>5.0)+(y<1.0))],'gx')

plt.show()