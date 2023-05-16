#convert wind direction and wind speed to u v wind and descide winde type
#Chih-Yen 1004

import numpy as np

#make a selfdefine function to read and convert the wind speed data
def convert2uv(ws,wd):
    u=-ws*np.sin(np.radians(wd))
    v=-ws*np.cos(np.radians(wd)) 
    return u,v


date,time,ws,wd=np.loadtxt('hw3_data.txt',skiprows=1,dtype='U5,U5,f8,f8',unpack='True')

#create a empty string array for wind type
Type=np.zeros(72,dtype='U2')

#use boolean array to descide the wind type
NE = (0 < wd) * (wd < 90)
SE = (90 < wd) * (wd < 180)
SW = (180 < wd) * (wd < 270)
NW = (270 < wd) * (wd < 360)
Type[NE]='NE'
Type[SE]='SE'
Type[SW]='SW'
Type[NW]='NW'

#sort the wind speed from biggest to smallest
wssorted=np.argsort(ws,kind='mergesort')
wssorted=wssorted[::-1]

#use selfdefine function to convert the wind speed and direction into u v wind
u,v=convert2uv(ws,wd)

#write the sorted and formated data
data=np.array(list(zip(date[wssorted],time[wssorted],ws[wssorted],u[wssorted],v[wssorted],Type[wssorted])),dtype=[('date','U5'),('time','U5'),('ws','f8'),('u','f8'),('v','f8'),('Type','U5')])
np.savetxt('hw4a.txt',data,fmt=('%5s','%5s','%6.3f','%8.3f','%6.3f','%2s'),header='Date  Time   WS[m/s] u[m/s] v[m/s] Type',comments=(''))

