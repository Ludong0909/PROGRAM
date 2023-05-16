import numpy as np 
import matplotlib.pyplot as plt

Rd = 287
Lv = 2.5*10**6
P0 = 1000
Cp = 1004
Rv = 461
P = np.linspace(700,1000,301)
Tha = 300*np.ones(150)
Thb = 290*np.ones(151)
Th = np.hstack((Tha,Thb))
qa = 0.001*np.ones(150)
qb = 0.01*np.ones(151)
q = np.hstack((qa,qb))

T = Th*(P/P0)**(Rd/Cp)
es = 6.11*np.exp((Lv/Rv)*(1/273-1/T))
qs = 0.6226*(es/(P-es))
RH = q/qs
e = 1/0.6226*q*P

f, ax = plt.subplots(2,2,sharey='row')
ax[0,0].set_xlim(260,320)
ax[0,0].set_ylim(1000,700)
ax[0,0].set_title('temperature (K)')
ax[0,0].set_xlabel('')
ax[0,0].set_ylabel('P(hPa)')
ax[0,0].plot(Th,P,'g--')
ax[0,0].plot(T,P,'r:')
ax[0,0].legend([r'$\theta$',r'T'],loc='upper right')

ax[0,1].set_xlim(0,0.020)
ax[0,1].set_ylim(1000,700)
ax[0,1].set_title('mixing ratio (kg/kg)')
ax[0,1].plot(q,P,'g--')
ax[0,1].plot(qs,P,'r:')
ax[0,1].legend([r'q',r'q$_{s}$'],loc='upper right')

ax[1,0].set_xlim(0,30)
ax[1,0].set_ylim(1000,700)
ax[1,0].set_xlabel('vapor pressure (hPa)')
ax[1,0].set_ylabel('P(hPa)')
ax[1,0].plot(e,P,'g--')
ax[1,0].plot(es,P,'r:')
ax[1,0].legend([r'e',r'e$_{s}$'],loc='upper right')

ax[1,1].set_xlim(0.0,2.0)
ax[1,1].set_ylim(1000,700)
ax[1,1].set_xlabel('relative humidity')
ax[1,1].set_ylabel('P(hPa)')
ax[1,1].plot(RH,P,'r-')
ax[1,1].plot(np.ones(301),P,'k:')

plt.savefig('mid108a.png')
plt.show()

