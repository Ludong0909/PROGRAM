import numpy as np
import matplotlib.pyplot as plt
import ASThermodynamicFunc as Myfunc

H,P,T,Rh = np.loadtxt(fname='46810-2018072200.edt.txt',dtype=float,usecols=(1,2,3,4),skiprows=3,delimiter=',',unpack=True)
T = T+273.15
Tmin = np.amin(T)
Tminind = np.argmin(T) #Find location of Tropopause)
TOT = H[Tminind]
Tparcel = T[0] - 9.8/1000*(H) #Temp. of Parcel
Tparcel10 = 10 + T[0] - 9.8/1000*(H) #Temp. of Parcel 10K higher

g = 9.80665 #[m/s^2]
es = Myfunc.SatuationWaterVaporPressure(T)
e = es*Rh #Water vapor pressure
qv = Myfunc.SpecificHumidity(P,e) 
Tv = Myfunc.VirtualTemperature(T,qv)
difference = Tv - T
fb = (Tparcel - Tv)*g/Tv
fb10 = (Tparcel10 - Tv)*g/Tv
plot2hlim = 0

for i in range(1,len(H)-1): #Find limit
    if (abs(Tv[i]-T[i])<0.1):
        plot2hlim = H[i]
        print('Tv-T = ',difference[i])
        break

print('Buoyancy at TOT= ',fb[Tminind],' N')
print('Buoyancy at 1km= ',fb[198],' N')
print('Difference lower than 0.1K at: ',plot2hlim,' m') 
print('TOT is: ',H[Tminind],' m')
print(fb[0])

plt.plot(T,H)
plt.plot(Tv,H)
plt.axhline(y=TOT,color = 'r')
plt.ylim(0,18000)
plt.legend(['Temperature','Virtual Temperature','Topopause'])
plt.xlabel('Temperature[K]')
plt.ylabel('Height[m]')
plt.title('Vertical Profile of Temperature(B) and Virtual Temperature(O) with Height')
plt.savefig('CA2_1')
plt.show()

plt.plot(difference,H)
plt.xlim(0,0.5)
plt.ylim(0,plot2hlim)
plt.legend(['Temperature difference'])
plt.xlabel('Difference[K]')
plt.ylabel('Height[m]')
plt.title('Vertical Profile of Difference between Virtual Temp. and Temp. with Height')
plt.savefig('CA2_2')
plt.show()

plt.plot(qv,H)
plt.axhline(y=TOT,color = 'r')
plt.xlim(0,0.0025)
plt.ylim(0,18000)
plt.legend(['Specific Humidity','Topopause'])
plt.xlabel('Specific Humidity[g/kg]')
plt.ylabel('Height[m]')
plt.title('Vertical Profile of Specific Humidity with Height')
plt.savefig('CA2_3')
plt.show()


f,ax = plt.subplots(1,3,sharey='row')
ax[0].plot(Rh,H)
ax[0].legend(['Relative Humidity(B)'])
ax[0].set_ylim(0,plot2hlim  )
ax[0].set_xlim(0,100)
ax[0].set_title('Vertical Profile of Relative Humidity \n with Height')
ax[0].set_xlabel('Relative Humidity[%]')
ax[0].set_ylabel('Height[m]')
#middle
ax[1].plot(Tv,H,'r')
ax[1].set_xlim(280,310)
ax[1].legend(['Virtual Temp.(R)'])
ax[1].set_title('Vertical Profile of Virtual Temp. \n with Height')
ax[1].set_xlabel('Virtual Temp.[K]')
#right
ax[2].plot(difference,H,'orange')
ax[2].set_xlim(0,0.5)
ax[2].legend(['Temperature difference(O)'])
ax[2].set_xlabel('Difference[K]')
ax[2].set_ylabel('Height[m]')
ax[2].set_title('Vertical Profile of Difference between \n Virtual Temp. and Temp. with Height')
plt.savefig('CA2_4')
plt.show()

plt.plot(fb,H)
plt.plot(fb10,H)
plt.axhline(y=TOT,color = 'r')
plt.axvline(x = 0,color = 'r',ls = '--')

plt.xlim(-0.5,0.5)
plt.ylim(0,1000)
plt.legend(['Buoyancy Force of Normal Parcel','Buoyancy Force of Parcel with Temp. 10K Higher'])
plt.xlabel('Buoyancy Force [N]')
plt.ylabel('Height[m]')
plt.title('Vertical Profile of Buoyancy Force of Dry Air Parcel with Height')
plt.savefig('CA2_5_5')
plt.show()


