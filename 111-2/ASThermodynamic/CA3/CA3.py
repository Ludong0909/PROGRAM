import numpy as np
import matplotlib.pyplot as plt
import ASThermodynamicFunc as ASf
import pandas as pd

# Open file and read the data
H,P,T,Rh = np.loadtxt(fname='46810-2018072200.edt.txt',dtype=float,usecols=(1,2,3,4),skiprows=3,delimiter=',',unpack=True)

# Turn T into Kelvin
T = T+273.15

Tmin = np.amin(T)
TOS = H[3321]  # Find location of Tropopause (Top of Stratosphere)

# Set perameters and compute data
Rd = 287  # [J/K*kg]
g0 = 9.80665  # [m/s^2]
es = ASf.SatuationWaterVaporPressure(T)
e = es*Rh  # Water vapor pressure
qv = ASf.SpecificHumidity(P,e) 
Tv = ASf.VirtualTemperature(T,qv)
theta = ASf.PotentialTemperature(T,P)
thetav = ASf.VurtualPotentialTemp(T,qv,P)

# Define dry air temp. with lapse rate
Tparcel = T[0] - 9.8/1000*(H)  # Temp. of Parcel
Tparcel10 = 10 + T[0] - 9.8/1000*(H)  # Temp. of Parcel 10K higher

"""
# Q1----------------------------------------------------
# Zoom in
'''
plt.plot(T,H)
plt.plot(Tv,H)
plt.plot(theta,H)
plt.plot(thetav,H)
'''
plt.plot(thetav - theta , H)
plt.plot(Tv - T, H)
plt.grid()
#plt.xlim(300, 302.5)
#plt.ylim(0,100)
plt.legend(['Temp.','Virtual Temp.','Potential Temp.', 'Virtual Potential Temp.'])
plt.axvline(0,color = 'r',ls = '--')
#plt.legend([r'($\theta_{v}$ - $\theta$) - (Tv - T)', 'x = 0'])
plt.xlabel('Temperature Difference[K]')
plt.ylabel('Height[m]')
plt.title('Vertical Profile of Virtual Temperature and Virtual Potential Temperature with Height')
#plt.title(r'Vertical Profile of ($\theta_{v}$ - $\theta$) - (Tv - T) with Height')

plt.savefig('CA3_1')
plt.show()
"""
# Q2-----------------------------------------------------
# there is 6788 pieces of data
# Find Topopause

# Compute lapse rate
Tlapse2 = np.zeros(len(T))
for i in range(len(T)-2):
    Tlapse2[i+1] = (T[i+2] - T[i])*1000/((H[i+2] - H[i]))

# Soomthen the lapse rate
df = pd.DataFrame(Tlapse2)
Tlapsesmooth = df.rolling(150).mean()

# Plotting
#plt.plot(9.8 + Tlapsesmooth, H)
plt.plot(  -Tlapsesmooth, H, 'orange')
plt.fill_between(x =(-20,20) ,y1 = TOS, y2 = TOS+1000, color = 'pink')
plt.text(x =10 ,y = TOS+200 ,s = 'Topopause')
plt.grid()
plt.xlim(-10,15 )
plt.ylim(0,)
#plt.legend(['$\Gamma_{d}$ - $\Gamma$', '$\Gamma$',  'Topopause'])
plt.legend([r'$\Gamma$', 'Topopause'])

plt.xlabel('Lapse Rate[K/km]')
plt.ylabel('Height[m]')
plt.title('Vertical Profile Env. Lapse Rate with Height')
plt.savefig('CA3_2')
plt.show()

"""
# Q3-----------------------------------------------------
# Calculate physical depth for each pressure interval
# Zoom in and Enlarge
depth = []
depth10 = []
h_ind = []
for p in range(1000, 50, -50):
    # Find indices of data points closest to the current pressure interval
    indices = np.where(((P >= p) & (P < p + 10)))

    # Compute mean values for temperature and height
    T_mean = np.mean(Tv[indices])
    T_mean10 = np.mean(Tv[indices]+10)
    z_mean = np.mean(H[indices])

    # Find the height in specific pressure
    h_ind.append(np.where(H == min(H[np.where((abs(P-p)<=1))])))

    # Compute physical depth using hypsometric equation
    depth.append(ASf.HypsometricEquation(p+10, p, T_mean))
    depth10.append(ASf.HypsometricEquation(p+10, p, T_mean10))

P_layer = np.linspace(1000,50,19)

# Plotting
#plt.plot(np.array(depth10)-np.array(depth),P_layer,'b-o')
plt.plot(np.array(depth),P_layer,'b-o')
plt.plot(depth10,P_layer,'r-o')
plt.legend(['10 hPa layer depth','10 hPa layrt depth with temp. 10 K warmer'])
#plt.legend(['Differience 10 hPa layer depth'])
plt.xlabel('Depth [m]')
plt.ylabel('Pressure interval section [hPa]')
plt.ylim(1000,0)
plt.yticks(np.linspace(1000,0,21))
plt.title('Profile of Depth of 10 hPa Layer in 50hPa Interval')
plt.grid()
plt.savefig('CA3_3')
plt.show()
"""