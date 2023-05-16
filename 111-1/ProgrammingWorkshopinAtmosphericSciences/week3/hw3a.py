import numpy as np

date,time,ws,wd=np.loadtxt('hw3_data.txt',skiprows=1,dtype='U5,U5,f8,f8',unpack='True')

u=-ws*np.sin(np.radians(wd))
v=-ws*np.cos(np.radians(wd))

rws=ws[0:24]
gws=ws[24:48]
bws=ws[48:72]

rwd=wd[0:24]
gwd=wd[24:48]
bwd=wd[48:72]

ru=u[0:24]
gu=u[24:48]
bu=u[48:72]

rv=v[0:24]
gv=v[24:48]
bv=v[48:72]

import matplotlib.pyplot as plt

t=np.linspace(0,23,24)
f,ax=plt.subplots(2,2,sharex='all',figsize=(10,6))

ax[0,0].set_xlim([0,24])
ax[0,0].set_ylim([0,8])
ax[0,0].set_yticks(np.linspace(0,8,5))
ax[0,0].set_title('Wind speed',fontsize=15)
ax[0,0].set_ylabel('(m/s)',fontsize=15)
ax[0,0].plot(t,rws,'r--')
ax[0,0].plot(t,gws,'g--')
ax[0,0].plot(t,bws,'b--')
ax[0,0].legend(['20171227','20171228','20171229'],loc='upper right')

ax[0,1].set_ylim([0,360])
ax[0,1].set_yticks(np.linspace(0,360,9))
ax[0,1].set_title('Wind direction',fontsize=15)
ax[0,1].set_ylabel('(degree)',fontsize=15)
ax[0,1].plot(t,rwd,'r--')
ax[0,1].plot(t,gwd,'g--')
ax[0,1].plot(t,bwd,'b--')

ax[1,0].set_xlim([0,24])
ax[1,0].set_ylim([-8,8])
ax[1,0].set_xticks(np.linspace(0,24,7))
ax[1,0].set_yticks(np.linspace(-8,8,9))
ax[1,0].set_title('U-component wind',fontsize=15)
ax[1,0].set_xlabel('Time(hour)',fontsize=15)
ax[1,0].set_ylabel('(m/s)',fontsize=15)
ax[1,0].plot(t,ru,'r--')
ax[1,0].plot(t,gu,'g--')
ax[1,0].plot(t,bu,'b--')

ax[1,1].set_ylim([-8,8])
ax[1,0].set_xticks(np.linspace(0,24,7))
ax[1,1].set_yticks(np.linspace(-8,8,9))
ax[1,1].set_title('V-component wind',fontsize=15)
ax[1,1].set_xlabel('Time(hour)',fontsize=15)
ax[1,1].set_ylabel('(m/s)',fontsize=15)
ax[1,1].plot(t,rv,'r--')
ax[1,1].plot(t,gv,'g--')
ax[1,1].plot(t,bv,'b--')

plt.savefig('hw3a.png')
plt.show()

data=np.array(list(zip(date,time,u,v,ws,wd)),dtype=[('date','U5'),('time','U5'),('u','f8'),('v','f8'),('ws','f8'),('wd','f8')])
np.savetxt('hw3a.txt',data,fmt=('%5s','%6s','%+4.2f','%+6.2f','%6.3f','%7.1f'),header='Date  Time  u[m/s] v[m/s] WS[m/s] WD[deg]',comments=(''))