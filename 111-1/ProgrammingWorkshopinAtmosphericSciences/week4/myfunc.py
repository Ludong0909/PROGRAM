def Esat(T):
    import numpy as np
    # set constants
    A1, A2, A3, A4, A5, A6 = 6.112, 17.67, 273.15, 29.65, 21.87, 7.66

    P,T,Q=np.loadtxt('P_T_Q2.txt',skiprows=1,unpack=True)
    Es=np.zeros(T.shape[0])

    Tn = T <= 0
    Tp = T >= 273.15
    Ti = 0 < T < 273.15

    Es[Tn]=-999.9
    Es[Ti]=A1*np.exp((A2*T[Ti]-A3)/(T[Ti]-A4))
    Es[Tp]=A1*np.exp(A5*(T[Tp]-A3)/(T[Tp]-A6))

    return(Es)
