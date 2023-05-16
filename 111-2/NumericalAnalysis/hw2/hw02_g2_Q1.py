import numpy as np

# set x.
x = np.array(0.00275)

# divide fx = (e^x-1)/x into two term.
fx1 = np.exp(x)/x
fx2 = 1/x

# calculate different precision of value.
fx1_16 = np.array(fx1,dtype=np.half)
fx1_32 = np.array(fx1,dtype=np.single)
fx1_64 = np.array(fx1,dtype=np.double)
fx1_128 = np.array(fx1,dtype=np.longdouble)
fx2_16 = np.array(fx2,dtype=np.half)
fx2_32 = np.array(fx2,dtype=np.single)
fx2_64 = np.array(fx2,dtype=np.double)
fx2_128 = np.array(fx2,dtype=np.longdouble)
fx16 = fx1_16-fx2_16
fx32 = fx1_32-fx2_32
fx64 = fx1_64-fx2_64
fx128 = fx1_128-fx2_128

# calculate the round 
roundfx = round((fx1-fx2),5)


print(roundfx)
print(fx1_16-fx2_16, fx1_32-fx2_32, fx1_64-fx2_64, fx1_128-fx2_128)

#calculate the relative error
relative16 = abs((fx16-roundfx)/roundfx)
relative32 = abs((fx32-roundfx)/roundfx)
relative64 = abs((fx64-roundfx)/roundfx)
relative128 = abs((fx128-roundfx)/roundfx)
print(relative16*100, relative32*100, relative64*100, relative128*100)

