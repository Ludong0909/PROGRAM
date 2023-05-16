import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors

#read the data
data = np.fromfile('hw4_TCCIP_precip.dat',dtype=np.float64).reshape(366,69,41)
data2 = np.fromfile('hw4_lsmask.dat',dtype=np.float32).reshape(1024,1024)
w,n = np.loadtxt('hw4_lsmask_lonlat.txt',skiprows=1,dtype=np.float32,unpack='True')

#creat the 1D array and meshgrid
x = np.linspace(120,122,41)
y = np.linspace(21.9,25.3,69)
xx,yy = np.meshgrid(x,y)
ww,nn = np.meshgrid(w,n)

#use boolean array to index invalid value and sum the whole year precipitation
p = data != -99.
datap = np.where(p,data,np.nan)
precip = np.sum(datap,axis=0)

#plot the figure of yearly accumulated precipitation in 2020 and set figure parameter 
cwb= (['#a0fffa', '#00cdff', '#0096ff', '#0069ff', '#329600', '#32ff00', '#ffff00', '#ffc800', '#ff9600', 
'#ff0000', '#c80000', '#a00000', '#96009b', '#c800d2', '#ff00f5', '#ffc8ff'])
plt.figure(figsize=(8.75,10))
CS = plt.contourf(x,y,precip,levels=np.linspace(500,4000,15),colors=cwb,extend='both')
plt.xticks(np.linspace(118,124,7,),fontsize=15)
plt.yticks(np.linspace(21,26,6),fontsize=15)
plt.xlim(118,124)
plt.ylim(21,26)
plt.xlabel('longtitude',fontsize=18)
plt.ylabel('latitude',fontsize=18)
plt.title(r'Yearly accumulated precipitation in 2020 (mm)',fontsize=18)
plt.colorbar(CS,orientation='horizontal',ticks=(np.linspace(500,4000,15)),pad=0.1)

#use given data to plot the shore of Taiwan and set figure parameter
shore = plt.contour(ww,nn,data2,levels=[0.5],linewidths=2.5,colors='k')

plt.savefig('hw4b_1.png')
plt.show()

#plot the figure of days of daily precipitation > 50 mm and set figure parameter 
precip50f = np.where(datap!=np.nan,datap,0)
precip50t = sum(precip50f>50)
cmap=plt.get_cmap('hot_r')
levels=[0,1,2,4,6,8,10,12,15,20,25,30,35]
norm = matplotlib.colors.BoundaryNorm(levels, ncolors = cmap.N) 
plt.figure(figsize=(8.75,10))
CS2 = plt.pcolormesh(x,y,precip50t,norm=norm,cmap=cmap)
plt.xticks(np.linspace(118,124,7,),fontsize=15)
plt.yticks(np.linspace(21,26,6),fontsize=15)
plt.xlim(118,124)
plt.ylim(21,26)
plt.xlabel('longtitude',fontsize=18)
plt.ylabel('latitude',fontsize=18)
plt.title(r'Days of daily precipitation > 50 mm',fontsize=18)
plt.colorbar(CS2,orientation='horizontal',pad=0.1)

#use given data to plot the shore of Taiwan and set figure parameter
shore = plt.contour(ww,nn,data2,levels=[0.5],linewidths=2.5,colors='k')


plt.savefig('hw4b_2.png')
plt.show()