import numpy as np
import matplotlib.pyplot as plt

prec = np.loadtxt('TCCIP_daily_precip_2018-2020.txt',skiprows=1)
day = np.arange(0,1096)
rainsort = np.argsort(prec)
rain10 = np.where(rainsort < 10 ,prec, np.nan)

plt.plot(day,prec,'b-',linewidth=1)
plt.plot(day,rainsort,'r*')
plt.title('TCCIP daily precipitation time series',fontsize=18)
plt.xlabel('Days',fontsize=15)
plt.ylabel('Rainfall [mm/day]',fontsize=15)
plt.xticks(np.linspace(0,1100,12))
plt.yticks(np.linspace(0,130,14))
plt.ylim(0,130)
plt.xlim(0,1100)
plt.savefig('midc1.png')
plt.show()

bins = np.linspace(0,130,14)
counts = np.zeros(len(bins)-1)



