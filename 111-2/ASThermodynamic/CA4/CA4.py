import numpy as np
import matplotlib.pyplot as plt
import Mog

# Open file and read the data
H,P,T,Rh = np.loadtxt(fname='46810-2018072200.edt.txt',dtype=float,usecols=(1,2,3,4),skiprows=3,delimiter=',',unpack=True)

# Turn T into Kelvin
T = T+273.15

Tmin = np.amin(T)
TOS = H[3371]  # Find location of Tropopause (Top of Stratosphere)

# Set perameters and compute data
Rd = 287  # [J/K*kg]
g0 = 9.80665  # [m/s^2]
Cp = 1004  # [J/K*kg]
es = Mog.SatuationWaterVaporPressure(T)
e = es*Rh  # Water vapor pressure
qv = Mog.SpecificHumidity(P,e) 
Tv = Mog.VirtualTemperature(T,qv)
theta = Mog.PotentialTemperature(T,P)
thetav = Mog.VirtualPotentialTemp(T,qv,P)
Sd = Mog.DryStaticEnergy(T, H)

# Define dry air temp. with lapse rate
Tparcel = T[0] - 9.8/1000*(H)  # Temp. of Parcel
Sdparcel = Mog.DryStaticEnergy(Tparcel, H)
Thetaparcel = Mog.PotentialTemperature(Tparcel, P)
Thetaparcelvalue = [Thetaparcel[0]] * len(Tparcel)
# Define line-shaped dry parcel
# Find 1km and Torpopause
onekm = np.where(H ==np.min(H[np.where(abs(H - 1000)<=0.01)]))  # 198
halfkm = np.where(H ==502)  # 93
Tropopause = np.where(H == 15274)  # 3173
Tropopausehalf = np.where(H == 14277)  # 2953

Thalf = Tparcel[94:2954]
Thetahalf = [Thetaparcel[94]] * len(Thetaparcel[94:2954])
Sdhalf = Sdparcel[94:2954]
Hhalf = H[94:2954]
Phalf = P[94:2954]

"""
# 1km Parcel Temps.
Parcel1km = np.array(H[:199])
SdT1km = np.array(Sdparcel[:199]/Cp)
T1km = np.array(Tparcel[:199])
Theta1km = np.array(Thetaparcel[:199])

# Tropopause Parcel Temps.
Parceltrop = np.array(H[3174:3371])
SdTtrop = np.array(Sdparcel[3174:3371]/Cp)
Ttrop = np.array(Tparcel[3174:3371])
Thetatrop = np.array(Thetaparcel[3174:3371])

# ENV. Temps. at tropopause
SdTENVtrop = np.array(Sd[3174:3371]/Cp)
TENVtrop = np.array(T[3174:3371])
ThetaENVtrop = np.array(theta[3174:3371])
"""

"""
# Q1------------------------------------------------------------------------------
# CA4_10
plt.plot(Sd,H)
plt.plot(Cp * theta, H)
plt.grid()
plt.xlim(300000, 340000)
plt.ylim(0,10000)
plt.axhline(TOS,color = 'r',ls = '--')
plt.legend(['Dry Static Energy',r'$C_{P} * \theta$', 'Tropopause'])
plt.xlabel('Dry Static Energy [J/kg]')
plt.ylabel('Height [m]')
plt.title('Vertical Profile of Dry Static Energy and Potential Temp. with Height')
plt.savefig('CA4_10')
plt.show()

# CA4_11
plt.plot(Cp * theta - Sd, H)
plt.grid()
#plt.xlim(250000, )
plt.ylim(0,35000)
plt.axhline(TOS,color = 'r',ls = '--')
plt.axvline(0,color = 'purple',ls = '--')
plt.text(x = 0, y = TOS+10000, s = ' X = 0')
plt.legend([r'$C_{P} * \theta$ - $S_{d}$', 'Tropopause'])
plt.xlabel('Dry Static Energy difference [J/kg]')
plt.ylabel('Height [m]')
plt.title('Vertical Profile of Difference between Dry Static Energy and Potential Temp. with Height')
plt.savefig('CA4_11')
plt.show()



# Q2--------------------------------------------------------------------------
# CA4_20
plt.plot(Tparcel , H)
plt.plot(Sdparcel/Cp, H)
plt.plot(Thetaparcel , H)

plt.grid()
plt.ylim(0,TOS+1000)
plt.xlim(130,310)
#plt.axhline(TOS,color = 'r',ls = '--')
plt.axvline(0,color = 'purple',ls = '--')
#plt.text(x = 0, y = TOS+10000, s = ' X = 0')
plt.legend(['Temp.', '$S_{d}/C_{P}$', r'$\theta$'])
plt.xlabel('Dry Static Energy difference [J/kg]')
plt.ylabel('Height [m]')
plt.title('Vertical Profile of Static Temp. and Potential Temp. with Height of a Dry Air Parcel')
plt.savefig('CA4_20')
plt.show()

plt.plot(T , H)
plt.plot(Sd/Cp, H)
plt.plot(theta , H)
plt.grid()
plt.ylim(0,TOS+1000)
plt.xlim(190,400)
#plt.axhline(TOS,color = 'r',ls = '--')
plt.axvline(0,color = 'purple',ls = '--')
#plt.text(x = 0, y = TOS+10000, s = ' X = 0')
plt.legend(['Temp.', '$S_{d}/C_{P}$', r'$\theta$'])
plt.xlabel('Dry Static Energy difference [J/kg]')
plt.ylabel('Height [m]')
plt.title('Vertical Profile of Static Temp. and Potential Temp. with Height of environment')
plt.savefig('CA4_21')
plt.show()

f,ax = plt.subplots(1,2,sharey='row')
ax[0].plot(Tparcel,H)
ax[0].plot(Sdparcel/Cp,H)
ax[0].plot(Thetaparcelvalue,H)
ax[0].legend(['Temp.', '$S_{d}/C_{P}$', r'$\theta$'])
ax[0].set_ylim(0,  TOS+1000)
ax[0].set_xlim(110,310)
ax[0].set_title('Vertical Profile of Static Temp. and Potential Temp.\n with Height of a Dry Air Parcel')
ax[0].set_xlabel('Temp. [K]')
ax[0].set_ylabel('Height[m]')
#right
ax[1].plot(T,H)
ax[1].plot(Sd/Cp,H)
ax[1].plot(theta,H)
ax[1].set_xlim(190,400)
ax[1].legend(['Temp.', '$S_{d}/C_{P}$', r'$\theta$'])
ax[1].set_ylim(0,  TOS+1000)
ax[1].set_title('Vertical Profile of Static Temp. and Potential Temp.\n with Height of environment')
ax[1].set_xlabel('Temp. [K]')

plt.savefig('CA4_22')
plt.show()

"""
# Q3--------------------------------------------------------------------------
#CA4_30

plt.plot(Thalf, Phalf, 'r')
plt.plot(Sdhalf/Cp, Phalf, 'green')
plt.plot(Thetahalf, Phalf, 'b')
plt.grid()
plt.xlim(300,302 )
plt.ylim(1000,0)
plt.axhline(P[3371],color = 'r',ls = '--')
plt.axhline(P[198],color = 'pink',ls = '--')
plt.text(x = 300.5, y = P[3371]-5, s = 'Tropopause')
plt.text(x = 300.5, y = P[198]-5, s = '1km')


plt.legend(['Temp.', '$S_{d}/C_{P}$', r'$\theta$', 'Tropopause'])
plt.xlabel('Temp. [K]')
plt.ylabel('Pressure [m]')
plt.title('Vertical Profile of Temps. of 1km Line-shaped Parcel \n hifted to Tropopause')
plt.savefig('CA4_30')
plt.show()



"""
plt.plot(T1km, Parcel1km, 'r')
plt.plot(SdT1km, Parcel1km, 'green')
plt.plot(Theta1km, Parcel1km, 'b')
plt.grid()
#plt.xlim(250000, )
plt.ylim(0,1100)
plt.axhline(TOS,color = 'r',ls = '--')
plt.axhline(1000,color = 'pink',ls = '--')
plt.text(x = 297, y = 1000-40, s = '1km')

plt.legend(['Temp.', '$S_{d}/C_{P}$', r'$\theta$', 'Tropopause'])
plt.xlabel('Temp. [K]')
plt.ylabel('Height [m]')
plt.title('Vertical Profile of Temps. of 1km Line-shaped Parcel at Surface')
plt.savefig('CA4_30')
plt.show()

#CA4_31
plt.plot(Ttrop, Parceltrop , 'r')
plt.plot(SdTtrop, Parceltrop , 'green')
plt.plot(Thetatrop, Parceltrop, 'b')
plt.plot(TENVtrop, Parceltrop , 'pink')
plt.plot(SdTENVtrop, Parceltrop, 'y')
plt.plot(ThetaENVtrop, Parceltrop, 'c')

plt.grid()
plt.xlim(100,)
plt.ylim(TOS-1000,)
plt.axhline(TOS,color = 'pink',ls = '--')
plt.text(x = 220, y = TOS-40, s = 'Tropopause')
plt.legend(['Temp.', '$S_{d}/C_{P}$', r'$\theta$', 'ENV. Temp.', 'ENV. $S_{d}/C_{P}$', r'ENV. $\theta$', 'Tropopause'])
plt.xlabel('Temp. [K]')
plt.ylabel('Height [m]')
plt.title('Vertical Profile of Temps. of 1km Line-shaped Parcel at 1km beneath Tropopause')
plt.savefig('CA4_31')
plt.show()

#CA4_32
plt.plot(TENVtrop - Ttrop, Parceltrop, 'r')
plt.plot( SdTENVtrop - SdTtrop, Parceltrop, 'green')
plt.plot(ThetaENVtrop - Thetatrop, Parceltrop, 'b')
plt.grid()
plt.xlim(40, )
plt.ylim(TOS-1000,)
plt.axhline(TOS,color = 'pink',ls = '--')
plt.text(x = 70, y = TOS-40, s = 'Tropopause')
plt.legend(['Temp.', '$S_{d}/C_{P}$', r'$\theta$', 'Tropopause'])
plt.xlabel('Temp. Difference [K]')
plt.ylabel('Height [m]')
plt.title('Vertical Profile of Temps. Difference between ENV. and 1km Line-shaped Parcel at 1km beneath Tropopause')
plt.savefig('CA4_32')
plt.show()

#CA4_33
plt.plot(TENVtrop - Ttrop, Parceltrop, 'r')
plt.grid()
#plt.xlim(40, )
plt.ylim(TOS-1000,)
plt.axhline(TOS,color = 'pink',ls = '--')
plt.text(x = 70, y = TOS-40, s = 'Tropopause')
plt.legend(['Temp.',  'Tropopause'])
plt.xlabel('Temp. Difference [K]')
plt.ylabel('Height [m]')
plt.title('Vertical Profile of Temps. Difference between ENV. and 1km Line-shaped Parcel at 1km beneath Tropopause')
plt.savefig('CA4_33')
plt.show()

#CA4_34
plt.plot( SdTENVtrop - SdTtrop, Parceltrop, 'green')
plt.grid()
#plt.xlim(40, )
plt.ylim(TOS-1000,)
plt.axhline(TOS,color = 'pink',ls = '--')
plt.text(x = 70, y = TOS-40, s = 'Tropopause')
plt.legend([ '$S_{d}/C_{P}$', 'Tropopause'])
plt.xlabel('Temp. Difference [K]')
plt.ylabel('Height [m]')
plt.title('Vertical Profile of Dry Static Temps. Difference between ENV. and 1km Line-shaped Parcel at 1km beneath Tropopause')
plt.savefig('CA4_34')
plt.show()

#CA4_35
plt.plot(ThetaENVtrop - Thetatrop, Parceltrop, 'b')
plt.grid()
#plt.xlim(40, )
plt.ylim(TOS-1000,)
plt.axhline(TOS,color = 'pink',ls = '--')
plt.text(x = 70, y = TOS-40, s = 'Tropopause')
plt.legend([r'$\theta$', 'Tropopause'])
plt.xlabel('Temp. Difference [K]')
plt.ylabel('Height [m]')
plt.title('Vertical Profile of Potential Temps. Difference between ENV. and 1km Line-shaped Parcel at 1km beneath Tropopause')
plt.savefig('CA4_35')
plt.show()
"""
