
import numpy as np
import matplotlib.pyplot as plt
import mog_angel as mog
import copy as c
from scipy.interpolate import interp1d

H_ini, P_ini, T_ini, qv_ini = np.loadtxt('CA8-2_data.txt',skiprows=1,usecols=(0,1,2,3),unpack=True,dtype=float)

H = np.linspace(0, 20000, 2001)
f1 = interp1d(H_ini, P_ini, kind = 'linear', fill_value = 'extrapolate')
f2 = interp1d(H_ini, T_ini, kind = 'linear', fill_value = 'extrapolate')
f3 = interp1d(H_ini, qv_ini, kind = 'linear', fill_value = 'extrapolate')
P = f1(H)
T = f2(H)
qv = f3(H)

es = mog.es(T)
qvs = mog.qvs(T, P)
Tv = mog.Tv(qv, T)
theta = mog.theta(T, P)

Cp = 1004
Lv = 2.5e6
Q = 0.12
R = 3e-5

# mixing layer
time = np.zeros(len(H))
qvm = np.zeros(len(H))
for i in range(len(H)):
    time[i] = (theta[i] * H[i] - np.trapz(theta[:i+1], H[:i+1])) / Q
    qvm[i] = (np.trapz(qv[:i+1], H[:i+1]) + R * time[i]) / H[i]

# time evolution
hr12 = time[:np.argmin(abs(time/3600 - 12))+1]
print(len(hr12))
LCL = np.zeros(len(hr12)).astype(int)
LFC = np.zeros(len(hr12)).astype(int)
EL = np.zeros(len(hr12)).astype(int)
H_LCL = np.zeros(len(hr12))
H_LFC = np.zeros(len(hr12))
H_EL = np.zeros(len(hr12))
CAPE= np.zeros(len(hr12))
CIN= np.zeros(len(hr12))

for hr in range(len(hr12)):

    # variables after heating
    T_heat = np.array(list(mog.inv_theta(theta[hr], P[:hr])) + list(T[hr:]))
    qv_heat = np.array(list(np.zeros(hr) + qvm[hr]) + list(qv[hr:]))
    qvs_heat = mog.qvs(T_heat, P)
    
    # find cloudbase and Tc
    condense = False
    for i in range(hr):
        if qv[hr] >= qvs_heat[i]:
            cloudbase = i
            Tc = T_heat[cloudbase]
            cloudbase = H[cloudbase]
            condense = True
    
            # variables after condensation
            T_cond = c.copy(T_heat)
            qv_cond = c.copy(qv_heat)
            tol =1e-7
            for j in range(int(cloudbase), int(hr)):
                x1 = T_heat[j]
                x2 = x1 + 50
                while(abs(x2 - x1) > tol):
                    if (qv[hr] - Cp/Lv * (x1 - T_heat[j]) - mog.qvs(x1, P[j])) * (qv[hr] - Cp/Lv * ((x1+x2)/2 - T_heat[j]) - mog.qvs((x1+x2)/2, P[j])) < 0:
                        x2 = (x1 + x2) / 2
                    else:
                        x1 = (x1 + x2) / 2
                T_cond[j] = (x1 + x2) / 2
                qv_cond[j] -= Cp / Lv * ((x1+x2)/2 - T_heat[j])
            qvs_cond = mog.qvs(T_cond, P)
            break

    # final T
    if condense == True:
        T_fin = T_cond
        qv_fin = qv_cond
        qvs_fin = qvs_cond
    else:
        T_fin = T_heat
        qv_fin = qv_heat
        qvs_fin = qvs_heat

    # Sd, hm, hms
    Sd = mog.Sd(T_fin, H)
    hm = mog.hm(T_fin, H, qv_fin)
    hms = mog.hms(T_fin, H, qvs_fin)
    
    # LCL
    p_T = np.zeros(len(H)) + T_fin[0] 
    p_qv = np.zeros(len(H)) + qv_fin[0]
    p_qvs = np.zeros(len(H)) + mog.qvs(p_T, p_qv)
    for i in range(1,len(H)):
        p_T[i] = mog.dry_lapse(p_T[i-1], H[i], H[i-1])
        p_qvs[i] = mog.qvs(p_T[i], P[i])
        if p_qv[i] >= p_qvs[i]:
            p_qv[i] = p_qvs[i]
            LCL[hr] = i
            H_LCL[hr] = H[i]
            break

    # LFC
    LFC_find = False
    for i in range(LCL[hr],len(H)):
        p_T[i] = mog.moist_lapse(p_T[i-1], H[i], H[i-1], p_qvs[i-1])
        p_qvs[i] = mog.qvs(p_T[i], P[i])
        p_qv[i] = p_qvs[i]
        if p_T[i] >= T_fin[i]:
            LFC_find = True
            LFC[hr] = i
            H_LFC[hr] = H[i]
            break
    if LFC_find == False:
        H_LFC[hr] = np.nan
    
    # EL
    EL_find = False
    for i in range(LFC[hr],len(H)):
        p_T[i] = mog.moist_lapse(p_T[i-1], H[i], H[i-1], p_qvs[i-1])
        p_qvs[i] = mog.qvs(p_T[i], P[i])
        p_qv[i] = p_qvs[i]
        if p_T[i] <= T_fin[i] and EL_find == False:
            EL_find = True
            EL[hr] = i
            H_EL[hr] = H[i]
    if EL_find == False:
        H_EL[hr] = np.nan

    # CAPE, CIN
    if LFC_find == False:
        CAPE[hr] = np.nan
        CIN[hr] = np.nan
    else:
        CAPE[hr] = mog.CAPE(LFC[hr], EL[hr], H, p_qv, qv_fin, p_T, T_fin)
        CIN[hr] = mog.CIN(LFC[hr], H, p_qv, qv_fin, p_T, T_fin)

    # Plot evolution
    f, ax = plt.subplots(figsize = (12,6))
    plt.plot(Sd/Cp, H)
    plt.plot(hm/Cp, H)
    plt.plot(hms/Cp, H)
    plt.axhline(H_LFC[hr], linestyle = '--', color = 'blue', alpha = 0.5)
    plt.axhline(H_EL[hr], linestyle = '--', color = 'blue', alpha = 0.5)
    plt.axhline(H_LCL[hr], linestyle = '--', color = 'blue', alpha = 0.5)
    plt.axhline(H[hr], linestyle = '--', color = 'black', alpha = 0.5)
    plt.text(360, H_LFC[hr]+200, 'LFC = %.1f m' %(H_LFC[hr]), fontsize = 8)
    plt.text(360, H_EL[hr]+200, 'EL = %.1f m' %(H_EL[hr]), fontsize = 8)
    plt.text(360, H_LCL[hr]+200, 'LCL = %.1f m' %(H_LCL[hr]), fontsize = 8)
    plt.text(360, H[hr]+100, 'PBL = %.1f m' %(H[hr]), fontsize = 8)
    plt.legend(['DSE_T', 'MSE_T', 'MSE*_T'], loc = 'lower left')
    plt.ylim(0,18000)
    plt.xlim(290,390)
    plt.xlabel('Temperature [K]')
    plt.ylabel('Height [m]')
    plt.title('Evolution of XSE_T in 12hr')
    plt.savefig(f'C:/Users/User/PROGRAM/111-2/ASThermodynamic/CA8/Energy/Energy{int(hr)}.png', dpi = 300)
    plt.clf()

    
    plt.plot(hr12[:hr]/3600, CAPE[:hr], 'red')
    plt.plot(hr12[:hr]/3600, CIN[:hr], 'blue')
    plt.text(hr12[hr]/3600 + 0.1, CAPE[hr], 'CAPE = %.1f J' %(CAPE[hr]), fontsize = 8)
    plt.text(hr12[hr]/3600 + 0.1, CIN[hr], 'CIN = %.1f J' %(CIN[hr]), fontsize = 8)
    plt.xlim([0,12])
    plt.grid()
    plt.ylim(-10,1400)
    plt.xlabel('Time [hr]')
    plt.ylabel('Energy [J/kg]')
    plt.legend(['CAPE', 'CIN'])
    plt.title('Evolution of CAPE and CIN in 12hr')
    plt.savefig(f'C:/Users/User/PROGRAM/111-2/ASThermodynamic/CA8/CAPE_CIN/CAPE_CIN{int(hr)}.png', dpi = 300)
    plt.clf()


    plt.plot(hr12[:hr]/3600, H_EL[:hr])
    plt.plot(hr12[:hr]/3600, H_LFC[:hr])
    plt.plot(hr12[:hr]/3600, H_LCL[:hr])
    plt.plot(time[:hr]/3600, H[:hr], 'k', alpha=0.7)
    plt.text(hr12[hr]/3600 + 0.1, H_EL[hr], 'EL = %.1f m' %(H_EL[hr]), fontsize = 8)
    plt.text(hr12[hr]/3600 + 0.1, H_LCL[hr]+200, 'LCL = %.1f m' %(H_LCL[hr]), fontsize = 8)
    plt.text(hr12[hr]/3600 + 0.1, H_LFC[hr]+500, 'LFC = %.1f m' %(H_LFC[hr]), fontsize = 8)
    plt.text(hr12[hr]/3600 + 0.1, H[hr]-200, 'PBL = %.1f m' %(H[hr]), fontsize = 8)
    plt.grid()
    plt.xlim([0,12])
    plt.ylim([0,13000])
    plt.xlabel('Time [hr]')
    plt.ylabel('Height [m]')
    plt.legend(['EL','LFC','LCL','PBL'], fontsize = 9, loc='upper left')
    plt.title('Evolution of LCL, LFC, EL in 12hr')
    plt.savefig(f'C:/Users/User/PROGRAM/111-2/ASThermodynamic/CA8/LEVELS/LEVELS{int(hr)}.png', dpi = 300)
    plt.clf()


plt.plot(hr12/3600, CAPE, 'red')
plt.plot(hr12/3600, CIN, 'blue')
plt.xlim([0,12])
plt.grid()
plt.xlabel('Time [hr]')
plt.ylabel('Energy [J/kg]')
plt.legend(['CAPE', 'CIN'])
plt.title('Evolution of CAPE and CIN in 12hr')
plt.savefig('2_CAPE_CIN_evolution.png', dpi=500)
plt.show()


plt.plot(hr12/3600, H_EL)
plt.plot(hr12/3600, H_LFC)
plt.plot(hr12/3600, H_LCL)
plt.plot(time/3600, H, 'k', alpha=0.7)
plt.grid()
plt.xlim([0,12])
plt.ylim([0,14000])
plt.xlabel('Time [hr]')
plt.ylabel('Height [m]')
plt.legend(['EL','LFC','LCL','$H_m$'], fontsize = 9, loc='upper left')
plt.title('Evolution of $H_m$, LCL, LFC, EL in 12hr')
plt.savefig('2_time_evolution.png', dpi=500)
plt.show()