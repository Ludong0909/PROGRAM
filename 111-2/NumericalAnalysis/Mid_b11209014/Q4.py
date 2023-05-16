import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import Cheers

SW = np.linspace(0.02,0.38,15,dtype=float)
EF = np.array([0.153,0.308,0.532,0.712,0.767,0.922,0.912,0.955,0.945,0.939,0.988,0.989,0.987,1.012,1.018],dtype=float)
ln_SW = np.log(SW)
ln_EF = np.log(EF)

def RMS (RL,Real):
    rms = (sum((RL-Real)**2)/len(RL))**(0.5)
    return(rms)

def RMS2 (RL3,RL4,Real3,Real4):
    square = (sum((RL3-Real3)**2) + sum((RL4-Real4)**2))/len(RL)
    rms = square**(0.5)
    return rms


# Q4-1
coe = Cheers.Least_Square_Regression(SW,EF)
RL = Cheers.Regression_Line(SW,coe)
print(coe)
print(RMS(RL,EF))

plt.plot(SW,EF,'o')
plt.plot(SW,RL)
plt.grid()
plt.savefig('Q4-1.png')
plt.show()


# Q4-2
coe2 = Cheers.Least_Square_Regression(ln_SW,ln_EF)
#RL2 = Cheers.Regression_Line(SW,[(coe2[0]),coe2[1]])
RL2 = np.exp((coe2[0] + coe2[1] * ln_SW))
print((coe2[0]),coe2[1])
print(RMS(RL2,EF))

plt.plot(SW,EF,'o')
plt.plot(SW,(RL2))
plt.grid()
plt.savefig('Q4-2.png')
plt.show()


# Q4-3
rms = []
for i in range(10):
    plt.plot(SW,EF,'o')
    coe3 = Cheers.Least_Square_Regression(SW[0:3+i],EF[0:3+i])
    coe4 = Cheers.Least_Square_Regression(SW[3+i:],EF[3+i:])
    RL3 = Cheers.Regression_Line(SW[0:3+i],coe3)
    RL4 = Cheers.Regression_Line(SW[3+i:],coe4)
    rms.append (RMS2(RL3, RL4, EF[0:3+i], EF[3+i:]))
    plt.plot(SW[0:3+i],RL3)
    plt.plot(SW[3+i:],RL4)
    plt.grid()
    plt.show()



print(min(rms),np.argmin(rms))
print(rms)