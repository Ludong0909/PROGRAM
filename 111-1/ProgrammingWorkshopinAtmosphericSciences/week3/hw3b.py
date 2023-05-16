import numpy as np
import matplotlib.pyplot as plt

#set parameter
S0=10000
I0=10
R0=0
B=0.0005
r=0.5

#create array and set initial value
S=np.zeros(501)
I=np.zeros(501)
R=np.zeros(501)
dt=np.ones(501)/100
t=np.linspace(0,5,501)
S[0]=S0
I[0]=I0
R[0]=R0

#Euler method 
for i in range(1,501):
    S[i]=S[i-1]-B*I[i-1]*S[i-1]*dt[i-1]
    I[i]=I[i-1]+(B*I[i-1]*S[i-1]-r*I[i-1])*dt[i-1]
    R[i]=R[i-1]+r*I[i-1]*dt[i-1]

#plot the chat and set parameter
plt.plot(t,S,'tab:orange')
plt.plot(t,I,'tab:green')
plt.plot(t,R,'tab:blue')
plt.title(r'S$_{0}$=10000, I$_{0}$=10, $\beta$=0.0005, $\gamma$=0.5',fontsize=15)
plt.xlim(0,5)
plt.ylim(0,12000)
plt.xlabel('Month',fontsize=15)
plt.ylabel('Population',fontsize=15)
plt.legend(['S','I','R'],loc='upper right',fontsize=15)

#save the chart and show it
plt.savefig('hw3.png')
plt.show()

