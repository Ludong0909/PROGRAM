import numpy as np 
def getLWP(thb,qb) :
    Rd = 287
    Lv = 2.5*10**6
    P0 = 1000
    Cp = 1004
    Rv = 461
    P = np.linspace(700,1000,301)

    Thb = thb*np.ones(151)
    qb = qb*np.ones(151)

    Tha = 300*np.ones(150)
    Th = np.hstack((Tha,Thb))
    qa = 0.001*np.ones(150)
    q = np.hstack((qa,qb))

    T = Th*(P/P0)**(Rd/Cp)
    es = 6.11*np.exp((Lv/Rv)*(1/273-1/T))
    qs = 0.6226*(es/(P-es))
    RH = q/qs

    i = RH > 1
    icloud = np.where(i,RH,np.nan)
    icb = np.nanargmin(icloud)
    ict = np.nanargmax(icloud)+1
    LWP = 100/9.8 * (np.trapz((q[ict:icb+1]-qs[ict:icb+1]),P[ict:icb+1]))
    return LWP