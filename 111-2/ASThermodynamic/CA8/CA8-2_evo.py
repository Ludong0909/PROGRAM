# -*- coding: utf-8 -*-
"""
Created on Fri May 26 22:45:17 2023

@author: 安柔
"""

import numpy as np
import matplotlib.pyplot as plt
import mog_angel as mog
import copy as c
from scipy.interpolate import interp1d

H_ini, P_ini, T_ini, qv_ini = np.loadtxt('CA8-1_data.txt',skiprows=1,usecols=(0,1,2,3),unpack=True,dtype=float)

H = np.linspace(0, 20000, 10001)
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

f, ax = plt.subplots(figsize = (12,8))
plt.plot(hr12/3600, CAPE, 'red')
plt.plot(hr12/3600, CIN, 'blue')
plt.xlim([0,12])
plt.grid()
plt.xlabel('time [hr]')
plt.ylabel('height [m]')
plt.title('Evolution of CAPE and CIN in 12hr')
plt.legend(['CAPE', 'CIN'])
plt.savefig('2_CAPE_evolution.png', dpi=500)
plt.show()

f, ax = plt.subplots(figsize = (12,8))
plt.plot(hr12/3600, H_EL)
plt.plot(hr12/3600, H_LFC)
plt.plot(hr12/3600, H_LCL)
plt.plot(time/3600, H, 'k', alpha=0.7)
plt.grid()
plt.xlim([0,12])
plt.ylim([0,14000])
plt.xlabel('time [hr]')
plt.ylabel('height [m]')
plt.legend(['EL','LFC','LCL','Hm'], fontsize = 9, loc='upper left')
plt.title('Evolution of $H_m$, LCL, LFC, EL in 12hr')
plt.savefig('2_time_evolution.png', dpi=500)
plt.show()