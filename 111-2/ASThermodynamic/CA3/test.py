import numpy as np
import matplotlib.pyplot as plt
p1 = np.array([np.linspace(1000,50,20)],dtype=float)
p2 = p1 - 10
print(np.log(p1/p2),p1)
plt.plot(np.log(p1/p2),p1,'ro')
plt.xlim(0,0.3)
plt.ylim(1000,0)
plt.title('Diagram of log(P/P-10) in P coordinate')
plt.xlabel('P/P-10')
plt.ylabel('P')
plt.grid()
plt.show()