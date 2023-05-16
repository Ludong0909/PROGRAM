import numpy as np 
import matplotlib.pyplot as plt
import mid109d_f as mf

Ps , height , Ts , RHs = np.loadtxt('midc_input.txt',skiprows=1,unpack='True')

CF=mf.cal_cf(Ps[Ps>=700],RHs[Ps>=700])
Psmask = Ps[Ps>=700][CF>20]
CFmask = CF[CF>20]
Pssort=np.argmin(Psmask)

plt.plot(CF,Ps[Ps>=700],'g-.')
plt.plot(CFmask,Psmask,'gd')
plt.plot(CFmask[Pssort],Psmask[Pssort],'rd')
plt.legend(['CF','CF>20%','top of CF>20%'],fontsize=12)
plt.ylim(1013,700)
plt.xlim(5,40)
plt.ylabel('Pressure (hPa)',fontsize=14)
plt.xlabel('CF (%)',fontsize=14)
plt.savefig('mid109d.png')
plt.show()