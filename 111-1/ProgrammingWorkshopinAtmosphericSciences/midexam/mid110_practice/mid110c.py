import numpy as np
import matplotlib.pyplot as plt
import RET 
import matplotlib.cm as cm

S = np.linspace(1300,1400,51)
ap = np.linspace(0.1,0.9,51)
Te = RET.myfunc_Te(S,ap)

Cs = plt.contourf(S,ap,Te,cmap=cm.inferno,levels=np.linspace(150,275,26))
plt.plot(1361,0.3,'ko')
plt.text(1361,0.25,'Earth')
plt.colorbar(Cs,orientation='vertical')
plt.title('Radiative Equibrium Temperature [K]')
plt.xlabel('$S_{\odot}$(W$m^{-2}$)')
plt.ylabel(r'$\alpha$'+r'$_{p}$')


plt.show()

