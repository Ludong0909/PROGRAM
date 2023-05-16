import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cloud 

ThBL = np.linspace(285,294,10)
qBL = np.linspace(0.01,0.0205,8)
LWP = []
xx,yy = np.meshgrid(ThBL,qBL)

for i in range(8):
    for j in range(10):
        L = cloud.getLWP(ThBL[j],qBL[i])
        LWP.append(L)

LWP = np.reshape(LWP,(8,10))
Cs = plt.contourf(yy,xx,LWP,cmap=cm.ocean,levels = np.linspace(0,20,11))
plt.title('LWP (kg/$m^{2}$)')
plt.xlabel('$q_{BL}$')
plt.ylabel(r'$\theta_{BL}$')
plt.colorbar(Cs,orientation = 'vertical')

plt.savefig('mid109c.png')
plt.show()