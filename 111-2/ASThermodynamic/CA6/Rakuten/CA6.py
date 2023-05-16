import mog
import copy as c
import numpy as np
import matplotlib.pyplot as plt

# input data
H, P, T, RH = np.loadtxt('46810-2018072200.edt.txt'
, delimiter = ',', skiprows = 3, unpack = True, usecols=[1,2,3,4])

# constant and calculation
Cp = 1004
Lv = 2.5e6
g = 9.8
T = T + 273.15
qv = mog.qv(RH, T, P)
theta = mog.theta(T, P)


# 6-1--------------------------------------------------------------------------------------------
Sd_T = T + g * H / Cp
hm_T = Sd_T + Lv / Cp * qv
S_sat_T = Sd_T + Lv / Cp * mog.qv_s(T, P)
hm_T_min_index = np.argmin(hm_T)
H_min_hm = H[hm_T_min_index]

plt.plot(Sd_T, H)
plt.plot(hm_T, H)
plt.plot(S_sat_T, H)
plt.axhline(H_min_hm, color = 'black', linestyle = '--')
plt.text(350, H_min_hm + 200, f'Lowest hm at {H_min_hm} m')
plt.xlim(300, 410)
plt.xlabel('temperature [K]')
plt.ylim(0, 20000)
plt.ylabel('height [m]')
plt.legend(['dry static Temp.', 'moist static Temp.', 'saturation moist static Temp.'])
plt.title('Different static temperature vs. height')
plt.grid()
plt.savefig('static_temp.png', dpi=500)
plt.show()

# hm hms vs qv
f,ax = plt.subplots(1,3,sharey='row')
ax[0].plot(hm_T - Sd_T,H,'orange')
ax[0].legend(['$h_m/C_p - S_d/C_p$'])
ax[0].set_ylim(0,20000)
#ax[0].set_xlim(310,450)
ax[0].set_title('Difference between $h_m/C_p$ and $S_d/C_p$')
ax[0].set_xlabel('temperature [K]')
ax[0].set_ylabel('Height[m]')

ax[1].plot(qv,H)
ax[1].plot(mog.qv_s(T,P),H,'blue')
ax[1].set_ylim(0,20000)
ax[1].set_xlim(-0.005,0.03)
ax[1].legend(['Specific humidity', 'Saturated Specific Humidity'])
ax[1].set_title('(Saturated) Specific Humidity')
ax[1].set_xlabel('Specific Humidity [kg/kg]')

ax[2].plot(S_sat_T - Sd_T,H,'green')
ax[2].legend(['$h_{ms}/C_p - S_d/C_p$'])
ax[2].set_ylim(0,20000)
#ax[2].set_xlim(310,450)
ax[2].set_title('Difference between $h_{ms}/C_p$ and $S_d/C_p$')
ax[2].set_xlabel('temperature [K]')
plt.show()

# 6-2--------------------------------------------------------------------------------------------
# Constant
# for CA6-2 Q4
Q = 0.03 # significant heat flux
R = 1.2e-4 * 1 # latent heat flux

# for CA6-2 Q5
RH = RH * 1  # relative humidity
qv = mog.qv(RH, T, P)


# Calculating Hm, qvm and mixing time
h_1500 = np.argmin(np.abs(H - 1500))
t_1500 = (theta[h_1500] * (H[h_1500] - H[0]) - np.trapz(theta[0:h_1500+1], H[0:h_1500+1])) / Q
qv_1500 = (np.trapz(qv[0:h_1500+1], H[0:h_1500+1]) + R * t_1500) / H[h_1500]
print('PBL needs', int(t_1500 // 3600), 'hr', round((t_1500 % 3600) / 60, 2), 'min for developing to 1500 m high.')

T_heat = np.array(list(mog.inv_theta(theta[h_1500], P[:h_1500])) + list(T[h_1500:]))
theta_heat = np.array([theta[h_1500]] * h_1500 + list(theta[h_1500:]))
qv_heat = np.array(list(np.zeros(h_1500) + qv_1500) + list(qv[h_1500:]))


# Search for cloud base
no_cond = True
for i in range(h_1500):
    if qv_1500 >= mog.qv_s(T_heat[i], P[i]):
        cloud_base = i
        no_cond = False
        break
if no_cond:
    for i in range(h_1500, len(RH)):
        if RH[i] == 100:
            cloud_base = i
            no_cond = False
            break
if no_cond:
    print('No cloud base (whole environment unsaturated)')
else:
    print('The height of cloud base is', H[cloud_base], 'm')


# Bisection Method dealing with condensation
tol = 1e-7
qv_cond = c.copy(qv_heat)
T_cond = c.copy(T_heat)
for i in range(cloud_base, h_1500):
    if no_cond:
        break
    x1 = T_heat[i]
    x2 = x1 + 50
    while(abs(x2 - x1) > tol):
        if (qv_1500 - Cp/Lv * (x1 - T_heat[i]) - mog.qv_s(x1, P[i])) * (qv_1500 - Cp/Lv * ((x1+x2)/2 - T_heat[i]) - mog.qv_s((x1+x2)/2, P[i])) < 0:
            x2 = (x1 + x2) / 2
        else:
            x1 = (x1 + x2) / 2
    qv_cond[i] += Cp / Lv * (T_heat[i] - (x1+x2)/2)
    T_cond[i] = (x1 + x2) / 2


print('Cloud Base Temperature (Tc):', T_cond[cloud_base], 'K')


# Calculating other variables
qt = np.array(([qv_1500] * h_1500 + list(qv[h_1500:])))
ql = qt - qv_cond
theta_cond = mog.theta(T_cond, P)
theta_e = mog.theta_e(theta_cond, qv_cond, T_cond)
theta_l = mog.theta_l(theta_cond, ql, T_cond)


# Plot the result
plt.plot(T, H, color='orange', linewidth=1, alpha=0.5)
plt.plot(T_heat, H, color='orange', linestyle='-.')
plt.plot(T_cond, H, color='orange')
plt.plot(theta, H, 'b', linewidth = 1, alpha = 0.5)
plt.plot(theta_heat, H, 'b-.')
plt.plot(theta_cond, H, 'b')
plt.plot(theta_l, H, 'pink', linewidth = 4, alpha = 0.5)
plt.axhline(H[cloud_base], color = 'k', linestyle = '--')
plt.text(310, H[cloud_base]+50, 'cloud base: '+str(H[cloud_base])+' m', fontsize=9)
plt.axhline(y = H[h_1500], color = 'k', linestyle = '--', alpha = 0.5)
plt.text(x = 310, y = H[308] + 50, s = 'Top of Mixing Layer', fontsize=9)
plt.xlim(285, 320)
plt.xlabel('Temperatue [K]')
plt.ylim(0, 2000)
plt.ylabel('Height [m]')
plt.legend(['$T_{env}$', '$T_{bef}$', '$T_{aft}$', r'$\theta_{env}$', r'$\theta_{bef}$', r'$\theta_{aft}$', r'$\theta_l$'], loc = 'center left')
plt.title(r'Temeprature and $\theta$ after heating and condensation')
plt.grid()
plt.savefig('theta_normal.png', dpi=500)
plt.show()

plt.plot(qv_cond, H, 'blue', alpha = 1)
plt.plot(ql, H, 'orange', alpha = 1)
plt.plot(qt, H, 'green', alpha = 1)
plt.axhline(H[cloud_base], color = 'k', linestyle = '--')
plt.text(0.005, H[cloud_base]+50, 'cloud base: '+str(H[cloud_base])+' m', fontsize=9)
plt.axhline(y = H[h_1500], color = 'k', linestyle = '--', alpha = 0.5)
plt.text(x = 0.005, y = H[308] + 50, s = 'Top of Mixing Layer', fontsize=9)
plt.xlim(-0.003, 0.035)
plt.ylim(0, 2000)
plt.grid()
plt.legend(['$q_v$', '$q_l$', '$q_t$'])
plt.xlabel('Specific Humidity [kg/kg]')
plt.ylabel('Height [m]')
plt.title('Specific Humiditys v.s. Height')
plt.show()

plt.plot(theta_cond, H, 'blue', alpha = 1)
plt.plot(theta_e, H, 'orange', alpha = 1)
plt.plot(theta_l, H, 'green', alpha = 1)
plt.axhline(H[cloud_base], color = 'k', linestyle = '--')
plt.text(320, H[cloud_base]+50, 'cloud base: '+str(H[cloud_base])+' m', fontsize=9)
plt.axhline(y = H[h_1500], color = 'k', linestyle = '--', alpha = 0.5)
plt.text(x = 320, y = H[308] + 50, s = 'Top of Mixing Layer', fontsize=9)
plt.xlim(290, 400)
plt.ylim(0, 2000)
plt.legend([r'$\theta$', r'$\theta_e$', r'$\theta_l$'])
plt.xlabel('Temperature [K]')
plt.ylabel('Height [m]')
plt.title('Potential Temperatures v.s. Height')
plt.grid()
plt.show()







'''
# R = 0.5 * R
# qv_1500 = (np.trapz(qv[0:h_1500+1], H[0:h_1500+1]) + R * t_1500) / H[h_1500]
# T_final = mog.inv_theta(Theta[h_1500], P[:h_1500])
# qv_final = np.zeros(h_1500) + qv_1500
# for i in range(h_1500):
#     if qv_1500 >= mog.qv_s(T_final[i], P[i]):
#         cloud_base = i
#         break
# print('The height of cloud base is', H[cloud_base], 'm')

# tol = 1e-7
# for i in range(cloud_base, h_1500):
#     x1 = T_final[i]
#     x2 = x1 + 50
#     while(abs(x2 - x1) > tol):
#         if (qv_1500 - Cp/Lv * (x1 - T_final[i]) - mog.qv_s(x1, P[i])) * (qv_1500 - Cp/Lv * ((x1+x2)/2 - T_final[i]) - mog.qv_s((x1+x2)/2, P[i])) < 0:
#             x2 = (x1 + x2) / 2
#         else:
#             x1 = (x1 + x2) / 2
#     qv_final[i] += Cp / Lv * (T_final[i] - (x1+x2)/2)
#     T_final[i] = (x1 + x2) / 2

# plt.plot(T_final, H[:h_1500])
# plt.show()
# plt.plot(qv_final, H[:h_1500])
# plt.show()
# T_final = np.array(list(T_final) + list(T[h_1500:]))
# qt = np.array(([qv_1500] * h_1500 + list(qv[h_1500:])))
# qv_final = np.array(list(qv_final) + list(qv[h_1500:]))
# ql = qt - qv_final
# theta_final = mog.theta(T_final, P)
# theta_e = mog.theta_e(theta_final, qv_final, T_final)
# theta_l = mog.theta_l(theta_final, ql, T_final)

# plt.plot(qv_final, H)
# plt.plot(ql, H)
# plt.plot(qt, H)
# plt.xlim(-0.001, 0.03)
# plt.ylim(0, 2000)
# plt.grid()
# plt.legend(['$q_v$', '$q_l$', '$q_t$'])
# plt.show()

# plt.plot(theta_e, H)
# plt.plot(theta_l, H)
# plt.xlim(300, 400)
# plt.ylim(0, 2000)
# plt.grid()
# plt.show()

# R = 0.4 * R
# qv_1500 = (np.trapz(qv[0:h_1500+1], H[0:h_1500+1]) + R * t_1500) / H[h_1500]
# T_final = mog.inv_theta(Theta[h_1500], P[:h_1500])
# qv_final = np.zeros(h_1500) + qv_1500
# for i in range(h_1500):
#     if qv_1500 >= mog.qv_s(T_final[i], P[i]):
#         cloud_base = i
#         break
# print('The height of cloud base is', H[cloud_base], 'm')

# tol = 1e-7
# for i in range(cloud_base, h_1500):
#     x1 = T_final[i]
#     x2 = x1 + 50
#     while(abs(x2 - x1) > tol):
#         if (qv_1500 - Cp/Lv * (x1 - T_final[i]) - mog.qv_s(x1, P[i])) * (qv_1500 - Cp/Lv * ((x1+x2)/2 - T_final[i]) - mog.qv_s((x1+x2)/2, P[i])) < 0:
#             x2 = (x1 + x2) / 2
#         else:
#             x1 = (x1 + x2) / 2
#     qv_final[i] += Cp / Lv * (T_final[i] - (x1+x2)/2)
#     T_final[i] = (x1 + x2) / 2

# plt.plot(T_final, H[:h_1500])
# plt.show()
# plt.plot(qv_final, H[:h_1500])
# plt.show()
# T_final = np.array(list(T_final) + list(T[h_1500:]))
# qt = np.array(([qv_1500] * h_1500 + list(qv[h_1500:])))
# qv_final = np.array(list(qv_final) + list(qv[h_1500:]))
# ql = qt - qv_final
# theta_final = mog.theta(T_final, P)
# theta_e = mog.theta_e(theta_final, qv_final, T_final)
# theta_l = mog.theta_l(theta_final, ql, T_final)

# plt.plot(qv_final, H)
# plt.plot(ql, H)
# plt.plot(qt, H)
# plt.xlim(-0.001, 0.03)
# plt.ylim(0, 2000)
# plt.grid()
# plt.legend(['$q_v$', '$q_l$', '$q_t$'])
# plt.show()

# plt.plot(theta_e, H)
# plt.plot(theta_l, H)
# plt.xlim(300, 400)
# plt.ylim(0, 2000)
# plt.grid()
# plt.show()

# R = 5 * R
# RH = 0.5 * RH
# qv = mog.qv(RH, T, P)
# qv_1500 = (np.trapz(qv[0:h_1500+1], H[0:h_1500+1]) + R * t_1500) / H[h_1500]
# T_final = mog.inv_theta(Theta[h_1500], P[:h_1500])
# qv_final = np.zeros(h_1500) + qv_1500
# for i in range(h_1500):
#     if qv_1500 >= mog.qv_s(T_final[i], P[i]):
#         cloud_base = i
#         break
# print('The height of cloud base is', H[cloud_base], 'm')

# tol = 1e-7
# for i in range(cloud_base, h_1500):
#     x1 = T_final[i]
#     x2 = x1 + 50
#     while(abs(x2 - x1) > tol):
#         if (qv_1500 - Cp/Lv * (x1 - T_final[i]) - mog.qv_s(x1, P[i])) * (qv_1500 - Cp/Lv * ((x1+x2)/2 - T_final[i]) - mog.qv_s((x1+x2)/2, P[i])) < 0:
#             x2 = (x1 + x2) / 2
#         else:
#             x1 = (x1 + x2) / 2
#     qv_final[i] += Cp / Lv * (T_final[i] - (x1+x2)/2)
#     T_final[i] = (x1 + x2) / 2

# plt.plot(T_final, H[:h_1500])
# plt.show()
# plt.plot(qv_final, H[:h_1500])
# plt.show()
# T_final = np.array(list(T_final) + list(T[h_1500:]))
# qt = np.array(([qv_1500] * h_1500 + list(qv[h_1500:])))
# qv_final = np.array(list(qv_final) + list(qv[h_1500:]))
# ql = qt - qv_final
# theta_final = mog.theta(T_final, P)
# theta_e = mog.theta_e(theta_final, qv_final, T_final)
# theta_l = mog.theta_l(theta_final, ql, T_final)

# plt.plot(qv_final, H)
# plt.plot(ql, H)
# plt.plot(qt, H)
# plt.xlim(-0.001, 0.03)
# plt.ylim(0, 2000)
# plt.grid()
# plt.legend(['$q_v$', '$q_l$', '$q_t$'])
# plt.show()

# plt.plot(theta_e, H)
# plt.plot(theta_l, H)
# plt.xlim(300, 400)
# plt.ylim(0, 2000)
# plt.grid()
# plt.show()

# RH = 0.4 * RH
# qv = mog.qv(RH, T, P)
# qv_1500 = (np.trapz(qv[0:h_1500+1], H[0:h_1500+1]) + R * t_1500) / H[h_1500]
# T_final = mog.inv_theta(Theta[h_1500], P[:h_1500])
# qv_final = np.zeros(h_1500) + qv_1500

# condition = 1
# for i in range(h_1500):
#     if qv_1500 >= mog.qv_s(T_final[i], P[i]):
#         cloud_base = i
#         break
#     if i == h_1500 - 1:
#         for j in range(len(RH)):
#             if RH[j] == 100:
#                 cloud_base = j
#                 break
#             if j == len(RH) - 1:
#                 print('No cloud base (whole environment unsaturated)')
#                 condition = 0
# if condition == 1:
#     print('The height of cloud base is', H[cloud_base], 'm')
#     tol = 1e-7
#     for i in range(cloud_base, h_1500):
#         x1 = T_final[i]
#         x2 = x1 + 50
#         while(abs(x2 - x1) > tol):
#             if (qv_1500 - Cp/Lv * (x1 - T_final[i]) - mog.qv_s(x1, P[i])) * (qv_1500 - Cp/Lv * ((x1+x2)/2 - T_final[i]) - mog.qv_s((x1+x2)/2, P[i])) < 0:
#                 x2 = (x1 + x2) / 2
#             else:
#                 x1 = (x1 + x2) / 2
#         qv_final[i] += Cp / Lv * (T_final[i] - (x1+x2)/2)
#         T_final[i] = (x1 + x2) / 2
   
# if condition == 0:
#     qv_final = [qv_final] * h_1500
#     T_final = mog.inv_theta(np.array([Theta[h_1500]] * h_1500), P[:h_1500])
    
# plt.plot(T_final, H[:h_1500])
# plt.show()
# plt.plot(qv_final, H[:h_1500])
# plt.show()
# T_final = np.array(list(T_final) + list(T[h_1500:]))
# qt = np.array(([qv_1500] * h_1500 + list(qv[h_1500:])))
# qv_final = np.array(qv_final + list(qv[h_1500:]))
# ql = qt - qv_final
# theta_final = mog.theta(T_final, P)
# theta_e = mog.theta_e(theta_final, qv_final, T_final)
# theta_l = mog.theta_l(theta_final, ql, T_final)

# plt.plot(qv_final, H)
# plt.plot(ql, H)
# plt.plot(qt, H)
# plt.xlim(-0.001, 0.03)
# plt.ylim(0, 2000)
# plt.grid()
# plt.legend(['$q_v$', '$q_l$', '$q_t$'])
# plt.show()

# plt.plot(theta_e, H)
# plt.plot(theta_l, H)
# plt.xlim(300, 400)
# plt.ylim(0, 2000)
# plt.grid()
# plt.show()
'''