import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import func 

theta = np.linspace(275,310,36)
P = np.linspace(850,1050,21)

es = func.func_SAT(theta,P)

xx,yy =np.meshgrid(theta,P)
Cs = plt.contour(xx,yy,es,levels =np.linspace(5.000,55.000,11) ,cmap = cm.hsv ,fontsize=15)

plt.title('e$_{S}$ (hPa)')
plt.xlabel(r'$\theta$ (K)',)
plt.ylabel('P (hPa)')
plt.clabel(Cs,inline=1,fontsize=12)

plt.show()
