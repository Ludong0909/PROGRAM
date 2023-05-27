import numpy as np
import Mog
import matplotlib.pyplot as plt
from scipy import interpolate as intp

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



for k in range(0,1440+1,20):


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

    plt.plot(Sd_target/Cp, H_env)
    plt.plot(hm_target/Cp, H_env)
    plt.plot(hms_target/Cp, H_env)
    plt.axhline(H_env[target_index], linestyle = '--', color = 'black', alpha = 0.5)
    plt.text(350, H_env[target_index]+200, 'PBL = %.1f m' %(H_env[target_index]))
    plt.legend(['DSE_T', 'MSE_T', 'MSE*_T'], loc = 'upper left')
    plt.ylim(0, 18000)
    plt.xlim(295,390)
    plt.xlabel('Temperature [K]')
    plt.ylabel('Height [m]')
    plt.title('Kinds of Static Energy Temp.')
    plt.savefig(f'C:/Users/User/PROGRAM/111-2/ASThermodynamic/CA8/Evolution/Evolution{int(k/20)}.png', dpi = 300)
    plt.clf()