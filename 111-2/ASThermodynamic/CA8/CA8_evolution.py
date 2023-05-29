import numpy as np
import Mog
import matplotlib.pyplot as plt
from scipy import interpolate as intp
import scipy.optimize as opt

# !!!NOTE!!! data is adjusted to ab. decreasing/increasing
H_env,P_env,T_env,qv_env = np.loadtxt(fname='CA8-1_data.txt',dtype=float,usecols=(0,1,2,3),skiprows=1,unpack=True)

# Do some interpolation
X = np.linspace(0,70,71)
Y = np.linspace(0,70,7001)
H_it = intp.interp1d(X, H_env)
P_it = intp.interp1d(X, P_env)
T_it = intp.interp1d(X, T_env)
qv_it = intp.interp1d(X, qv_env)

# variables after interpolate (70->7000)
H_env = H_it(Y)
P_env = P_it(Y)
T_env = T_it(Y)
qv_env = qv_it(Y)

# Set perameters
Q = 0.12  # sensible heat flux [mK/s]
R = 3e-5  # latent heat flux [(kg*m)/(kg*s)]
Rd = Mog.Rd  # [J/K*kg]
Rv = Mog.Rv  # [J/K*kg]
epsilon = Mog.epsilon
g0 = Mog.g0  # [m/s^2]
Cp = Mog.Cp  # [J/K*kg]
Lv = Mog.Lv  # [J/kg]
A = 2.53*10**9  # hPa
B = 5.42*10**3  # K

# Compute variables
es_env = Mog.SaturationWaterVaporPressure(T_env)
qvs_env = Mog.SpecificHumidity(P_env, es_env)
theta_env = Mog.PotentialTemp(T_env,P_env)
hm_env = Mog.MoistStaticEnergy(T_env, H_env, qv_env)
hms_env = Mog.MoistStaticEnergy(T_env, H_env, qvs_env)
Sd_env = Mog.DryStaticEnergy(T_env, H_env)


for k in range(0,720+1,20):

    # time length
    duration = k

    # for comlutation
    thetam = theta_env
    qvv = qv_env

    # to store computation
    H_mix = np.zeros(duration + 1)
    theta_mix = np.zeros(duration + 1)
    qv_mix = np.zeros(duration + 1)
    time_index = np.zeros(duration + 1)

    # Use min as time unit
    for t in range(duration + 1):
        Qt = Q * t * 60
        Rt = R * t * 60

        # initial
        thetas = thetam[0] * H_env[0]  # integral of hm*thetam
        thetamm = thetam[0]  # for record
        qvs = qvv[0] * H_env[0]  # integral of hm*qvm

        for i in range(len(H_env)):

            if (thetamm * H_env[i] - thetas >= Qt):
                H_mix[t] = H_env[i]
                theta_mix[t] = thetamm
                qv_mix[t] = (qvs + Rt)/H_mix[t]
                time_index[t] = i
                break
            
            else:
                if (thetam[i+1] < thetamm):
                    thetamm = thetamm
                else:
                    thetamm = thetam[i+1]
            
            thetas += (thetam[i] + thetam[i+1]) * (H_env[i+1] - H_env[i]) * 0.5
            qvs += (qvv[i] + qvv[i+1])*(H_env[i+1] - H_env[i]) * 0.5

    time_index = np.int_(time_index)  # turn index to integer

    Sd_mix = Mog.DryStaticEnergy(T_env[time_index], H_env[time_index])
    hm_mix = Mog.MoistStaticEnergy(T_env[time_index], H_env[time_index], qv_mix)
    hms_mix = Mog.SaturatedMoistStaticEnergy(T_env[time_index], H_env[time_index], qv_mix)

    # Plot Sd, Hm, Hms, at targeted time
    target_index = time_index[-1]

    # Variables in PBL
    # T
    T_in_pbl = theta_mix[-1] * np.ones(target_index) /  ((1000/P_env[:target_index])**(Rd/Cp))
    # Sd
    Sd_target = Sd_env.copy()
    Sd_target[:target_index] = np.ones(target_index) * Sd_env[target_index]
    # hm
    hm_target = hm_env.copy()
    hm_target[:target_index] = np.ones(target_index) * hm_mix[-1]
    # hms
    hms_target = hms_env.copy()
    hms_in_pbl = np.ones(target_index) * Sd_env[target_index] + Lv * Mog.SaturatedSpecificHumidity(T_in_pbl, P_env[:target_index])
    hms_target[:target_index] = np.ones(target_index) * hms_in_pbl
    # qv
    qv_target = qv_env.copy()
    qv_target[:target_index] = np.ones(target_index) * qv_mix[-1]

    # Compute Tc
    def Solve_Tc(Tc):

        '''
        Using numerical method to find Tc
        
        ***Variables below need to be define before calculation.***
        '''

        # Set the values of the variables used in the function
        qvi = qv_env[target_index]
        P0 = P_env[target_index]
        T0 = T_env[target_index]
        epsilon = 0.622
        A = 2.53*10**9
        B = 5420
        kp = Cp/Rd

        # Calculate the value of the function and return it
        f = Tc - B/np.log(((A*epsilon)/(qvi*P0))*(T0/Tc)**kp)
        return f
    Tc = opt.bisect(Solve_Tc, 200, 400)
    LCL = (T_env[target_index] - Tc)/(g0/Cp) + H_env[target_index]
    LCL_index = np.where(np.abs(H_env - LCL)<1)[0][0]
    print('LCL = %.1f m'%LCL)

    # Compute Tv
    Tv_target = Mog.VirtualTemp(T_env[time_index], qv_env[time_index])
    thetav = Mog.VirtualPotentialTemp(T_env[time_index], qv_env[time_index], P_env[time_index])

    # Compute Gamma_m line
    T_moist = np.array([Tc],dtype=float)
    for i in range(1,len(H_env)-LCL_index):
        dH = H_env[i] - H_env[i-1]
        gamma_m = Mog.Gamma_m(T_moist[i-1], qvs_env[LCL_index+i-1])
        T_moist = np.append(T_moist, T_moist[-1] - dH*gamma_m)
    T_parcel = T_env.copy()
    T_parcel[LCL_index:] = T_moist

    # Find LFC, EL
    # LFC
    for i in range(len(T_parcel)):
        if T_parcel[i] > T_env[i]:
            LFC = H_env[i]
            LFC_index = i
            break
    # EL
    for i in range(LFC_index,len(T_parcel)):
        if T_env[i] > T_parcel[i]:
            EL = H_env[i]
            break
    LFC_index = np.where(np.abs(H_env - LFC)<1)[0][0]
    EL_index = np.where(np.abs(H_env - EL)<1)[0][0]
    print('LFC = %.1f m'%LFC)
    print('EL = %.1f m'%EL)

    # Compute Parcel Route (T_parcel = T_in_pbl + T_dry + T_moist)
    T_parcel[:target_index] = T_in_pbl
    T_dry = np.linspace(T_parcel[target_index], T_parcel[LCL_index], LCL_index-target_index)
    T_parcel[target_index:LCL_index] = T_dry

    # Compute Tv and Tv'
    Tv_parcel = Mog.VirtualTemp(T_parcel, qv_target)
    Tv_env = Mog.VirtualTemp(T_env, qv_env)

    # Compute CIN
    CIN_curve = (Tv_env[target_index:LFC_index] - Tv_parcel[target_index:LFC_index])/Tv_env[target_index:LFC_index] * g0
    CIN = np.trapz(CIN_curve)
    print('CIN = %.1f J'%CIN)

    # Compute CAPE
    CAPE_curve = (Tv_parcel[LFC_index:EL_index] - Tv_env[LFC_index:EL_index])/Tv_env[LFC_index:EL_index] * g0
    CAPE = np.trapz(CAPE_curve)
    print('CAPE = %.1f J'%CAPE)

    # Plot
    f, ax = plt.subplots(figsize = (12,6))
    plt.plot(T_parcel, H_env)
    plt.plot(T_env, H_env)
    plt.plot(Sd_target/Cp, H_env)
    plt.plot(hm_target/Cp, H_env)
    plt.plot(hms_target/Cp, H_env)
    plt.axhline(LFC, linestyle = '--', color = 'blue', alpha = 0.5)
    plt.axhline(EL, linestyle = '--', color = 'blue', alpha = 0.5)
    plt.axhline(LCL, linestyle = '--', color = 'blue', alpha = 0.5)
    plt.axhline(H_env[target_index], linestyle = '--', color = 'black', alpha = 0.5)
    plt.text(295, LFC+200, 'LFC = %.1f m' %(LFC), fontsize = 8)
    plt.text(295, EL+200, 'EL = %.1f m' %(EL), fontsize = 8)
    plt.text(295, LCL+200, 'LCL = %.1f m' %(LCL), fontsize = 8)
    plt.text(295, H_env[target_index]+100, 'PBL = %.1f m' %(H_env[target_index]), fontsize = 8)
    plt.legend(['T_parcel', 'T_env', 'DSE', 'MSE', 'MSE*'], loc = 'lower left')
    plt.ylim(0,18000)
    plt.xlim(175,390)
    plt.savefig(f'C:/Users/User/PROGRAM/111-2/ASThermodynamic/CA8/Evolution/Evolution{int(k/20)}.png', dpi = 300)
    plt.clf()