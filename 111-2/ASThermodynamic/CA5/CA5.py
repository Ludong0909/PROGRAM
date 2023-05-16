def f(qvc):
    Tc = T0 + ((qv0-qvc)*mog.Lv)/mog.Cp
    f = qvc - mog.ep*mog.CCeq(Tc)/P0
    return f
qvm1 = qvm0.copy()
qvs1 = qvs0.copy()
qvc = np.zeros(index_m)
print(hm0[np.where(qvm0>qvs0)[0][0]])
for i in range(np.where(qvm0>qvs0)[0][0],np.where(qvm0>qvs0)[0][-1]+1):
    global T0,qv0,P0
    T0 = Tm0[i]; qv0 = qvm0[i]; P0 = Pres[i]
    qvm1[i] = cheers.BisectionRoot(f,0,0,0.03,1e-7)
    qvs1[i] = cheers.BisectionRoot(f,0,0,0.03,1e-7)
    qvc[i] = cheers.BisectionRoot(f,0,0,0.03,1e-7)
qvc_draw = qvc.copy()
qvc[qvc==0] = qvm0[qvc==0]
qvc_draw[qvc_draw==0] = np.nan
Tc = Tm0 + ((qvm0-qvc)*mog.Lv)/mog.Cp
thc = mog.PotentialTemp(Tc,Pres[:230])