#CA0 for course atmospheric thermodynamic
import numpy as np
import matplotlib.pyplot as plt

#setting the parameter
P0 = 1000
Rd = 287
Cp = 1004

#open the file and calculate theata
P,H,T = np.loadtxt(fname='ishgaki_20150913_00z.txt',dtype=float,usecols=(0,1,2),skiprows=4,unpack=True)
T = T + 273.15
theata = T*((P0/P)**(Rd/Cp))

#Temperature,Theata with Pressure
plt.plot(T,P)
plt.plot(theata,P)
plt.ylim([1014,72.6])
for i in range (1,60):
        if  (T[i-1]>=T[i]) and (T[i]<T[i+1]):
            plt.axhline(y=P[i],color='r')
            print(P[i])
        if  (T[i-2]<T[i-1]) and (T[i-1]>=T[i]):
            plt.axhline(y=P[i-1],color='g')
            print(P[i-1])
plt.legend(['Temperature','Potential Temperature','Inversion Layer(end)','Inversion Layer(start)'])
plt.xlabel('Temperature[K]')
plt.ylabel('Pressure[hPa]')
plt.title('Vertical Profile of Temperature(B) and Potential Temperature(O) with Pressure, Marked the Inversion Layer(R,G)')
plt.savefig('CA0_1')
plt.show()

#Temperature,Theata with Height
plt.plot(T,H)
plt.plot(theata,H)
plt.ylim([7,18522])
for i in range (1,60):
        if  (T[i-1]>=T[i]) and (T[i]<T[i+1]):
            plt.axhline(y=H[i],color='r')
            print('H ',H[i])
        if  (T[i-2]<T[i-1]) and (T[i-1]>=T[i]):
            plt.axhline(y=H[i-1],color='g')
            print('H ',H[i-1])
plt.legend(['Temperature','Potential Temperature','Inversion Layer(end)','Inversion Layer(start)'])
plt.xlabel('Temperature[K]')
plt.ylabel('Height[m]')
plt.title('Vertical Profile of Temperature(B) and Potential Temperature(O) with Height, Marked the Inversion Layer(R,G)')
plt.savefig('CA0_2')
plt.show()