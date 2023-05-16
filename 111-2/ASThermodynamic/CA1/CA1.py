#CA1 for course AT
#Created on 2023/02/23 by CY-Tsai

import numpy as np
import matplotlib.pyplot as plt

P0 = 1000
Rd = 287
Cp = 1004

H,P,T,Rh = np.loadtxt(fname='46810-2018072200.edt.txt',dtype=float,usecols=(1,2,3,4),skiprows=3,delimiter=',',unpack=True)
T = T+273.15
theata = T*((P0/P)**(Rd/Cp))
Tmin = np.amin(T)
Tminind = np.argmin(T)
print(Tmin,P[Tminind],H[Tminind])

def dew_point_temperature(T, RH):

    """
    Calculates the dew point temperature given the temperature in Kelvin and relative humidity in percentage
    using the Magnus formula.

    Args:
    T (float): Temperature in Kelvin
    RH (float): Relative humidity in percentage (between 0 and 100)

    Returns:
    float: Dew point temperature in Kelvin
    """
    a = 17.27
    b = 237.7

    alpha = ((a * T) / (b + T)) + np.log(RH/100.0)
    dew_point = (b * alpha) / (a - alpha)

    return dew_point

Td = dew_point_temperature(T,Rh)
print(Td)

for i in range(1,6000):
    if abs((T[i]-Td[i])<1) :
        print(T[i],H[i],P[i])
 
#fig.1
f,ax = plt.subplots(1,2,sharey='row')
ax[0].set_yscale('log')
ax[0].plot(T,P)
ax[0].plot(Td,P)

ax[0].plot(T[Tminind],P[Tminind],'r*')
ax[0].legend(['Temperature(B)','The Dew Point Temperature(O)','The Lowest Temperature'])
ax[0].set_ylim(1003.4,6.2)
ax[0].set_xlim(0,350)
ax[0].set_title('Vertical Profile of Temperature with Pressure')
ax[0].set_xlabel('Temperature[K]')
ax[0].set_ylabel('Pressure in Log scale [hPa]')
#right
ax[1].plot(Rh,P,'r')
ax[1].set_xlim(0,100)
ax[1].legend(['Relative Humidity(R)'])
ax[1].set_title('Vertical Profile of Relative Humidity with Pressure')
ax[1].set_xlabel('Relative Humidity[%]')
plt.savefig('CA1_1.png')


#fig.2
f,bx = plt.subplots(1,2,sharey='row')
bx[0].plot(T,H)
bx[0].plot(Td,H)
bx[0].plot(T[Tminind],H[Tminind],'r*')
bx[0].legend(['Temperature(B)','The Dew Point Temperature(O)','The Lowest Temperature'])
bx[0].set_ylim(4,34452)
bx[0].set_xlim(0,350)
bx[0].set_title('Vertical Profile of Temperature with Height')
bx[0].set_xlabel('Temperature[K]')
bx[0].set_ylabel('Height[m]')
#right
bx[1].plot(Rh,H,'r')
bx[1].set_xlim(0,100)
bx[1].legend(['Relative Humidity(R)'])
bx[1].set_title('Vertical Profile of Relative Humidity with Height')
bx[1].set_xlabel('Relative Humidity[%]')
plt.savefig('CA1_2.png')

plt.show()