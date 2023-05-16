import numpy as np
import matplotlib.pyplot as plt
import Cheers

X = np.linspace(0,6,16,dtype=float)
Y = np.array([0,3,4.5,5.8,4.8,4.5,6.2,7.4,9.6,15.6,23.4,26.7,31.1,37.2,39.3,47.8],dtype=float)

third = Cheers.poly_regress(X,Y,3)
sixth = Cheers.poly_regress(X,Y,6)
ninth = Cheers.poly_regress(X,Y,9)
twe = Cheers.poly_regress(X,Y,12)
fif = Cheers.poly_regress(X,Y,15)

print(third)
print(sixth)
print(ninth)


cXY = Cheers.poly_regress(X,Y,5)
RL = Cheers.Regression_Line(X,cXY)

plt.plot(X,Y,'o')
plt.plot(X,RL)
plt.grid()
plt.show()