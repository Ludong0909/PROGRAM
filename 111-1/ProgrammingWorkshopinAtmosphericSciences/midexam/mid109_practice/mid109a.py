import math as m
import numpy as np 

#(a)
n = input('please input n(>=0)')

sn = 0
a = 1
for i in range(int(n)+1) :
    a = 1
    for b in range(i) :
        a = a/(1*(b+1))
    sn = sn + a 
print(sn)
print(m.exp(1))

error = abs(sn-m.exp(1))



