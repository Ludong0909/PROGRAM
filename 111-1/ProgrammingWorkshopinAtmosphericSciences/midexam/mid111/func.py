import numpy as np


Lv = 2.5*10**6
Rv = 461.0
Rd = 287
Cp = 1004.0
P0 = 1000

def func_SAT(theta,P) :
    t , p =np.meshgrid(theta,P)
    T = t*(p/P0)**(Rd/Cp)
    es = 6.11*np.exp((Lv/Rv)*(1/273-1/T))
    return es