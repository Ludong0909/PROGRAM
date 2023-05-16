import numpy as np

def myfunc_Te(S,ap) :
    O = 5.67*10**-8
    ss,aa =np.meshgrid(S,ap)
    Te = (((np.array(ss))/(4*O))*(1-np.array(aa)))**(1/4)
    return np.array(Te)