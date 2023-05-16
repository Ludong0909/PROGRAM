import numpy as np 

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

i = RH > 1
icloud = np.where(i,RH,np.nan)
icb = np.nanargmin(icloud)
ict = np.nanargmax(icloud)+1
LWP = 100/9.8 * (np.trapz((q[ict:icb+1]-qs[ict:icb+1]),x=P[ict:icb+1]))

print(' Pcb (hPa) = ',P[icb],'\n','Pct (hPa) = ',P[ict],'\n','LWP (kg/m2) = ','%4.2f'%LWP)

data=np.array(list(zip(P,Th,q,RH)),dtype=[('P','f8'),('Th','f8'),('q','f8'),('RH','f8')])
np.savetxt('mid108b.txt',data,fmt='%8.1f%8.1f%9.3f%9.3f',header='P(hPa)   Th(K)    q(kg/kg) RH',)