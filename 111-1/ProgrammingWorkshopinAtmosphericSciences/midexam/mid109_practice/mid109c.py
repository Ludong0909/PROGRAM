import numpy as np 
import matplotlib.pyplot as plt

Ps , height , Ts , RHs = np.loadtxt('midc_input.txt',skiprows=1,unpack='True')

f,ax = plt.subplots(1,2,sharey='all')
ax[0].plot(Ts,Ps,'k-o')
ax[1].plot(RHs,Ps,'b--')

ax[0].set_ylim(1013,500)
ax[0].set_xlim(-5,30)
ax[1].set_xlim(30,100)
ax[0].set_xlabel('Temperature (°C)',fontsize=14)
ax[1].set_xlabel('RH (%)',fontsize=14)
ax[0].set_ylabel('Pressure (hPa)',fontsize=14)

plt.savefig('mid109c.png')
plt.show()
