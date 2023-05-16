import numpy as np
import matplotlib.pyplot as plt

T0 = 298
q0 = 0.015
z = np.linspace(0,12000,601)
P0 = 1000
H = 8000
g = 9.8
cp = 1004
Lv = 2.5*10**6
Rv = 461.5
E = 0.622
Rd = 287

q00 = 15*np.ones(601)
P = P0 * np.exp(-z/H)
Tp = T0 + (-g/cp)*z 
es = 6.11*np.exp(Lv/Rv*(1/273.15-1/Tp))
qvs = E*es/(P-(1-E)*es)
Thp = Tp*(P0/P)**(Rd/cp)

q1 = q0 - qvs
iqv= (q0 - qvs) > 0
LCL = np.where(iqv,qvs,np.nan)
LCLloc = np.nanargmax(LCL)

print(qvs[iqv])
f, ax = plt.subplots(1,3,sharey='all')
ax[0].plot(Thp,z,'g--')
ax[0].plot(Tp,z,'r-.')
ax[0].set_xlim(180,300)
ax[0].set_ylim(0,12000)
ax[0].set_title('temperature')
ax[0].set_ylabel('height [m]')
ax[0].set_xlabel('[K]')
ax[0].set_xticks([180,210,240,270,300])

ax[1].plot(1000*qvs,z,'r-')
ax[1].plot(q00,z,'k:')
ax[1].plot(1000*q0,z[LCLloc],'bo')
ax[1].set_xlim(0,20)
ax[1].set_title('mixing ratio')
ax[1].legend([r'$q_{vsp}$',r'$q_{0}$','LCL'])
ax[1].set_xlabel('[g/kg]')
ax[1].set_xticks([0,5,10,15,20])


ax[2].plot(P,z,'k')
ax[2].set_xlim(200,1000)
ax[2].set_title('pressure')
ax[2].set_xlabel('[hPa]')
ax[2].set_xticks([200,400,600,800,1000])

plt.show()