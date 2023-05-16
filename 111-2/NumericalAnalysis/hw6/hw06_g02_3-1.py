import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

T0 = np.array([3,6,9,12,15,18,21,24],dtype=np.float64)
Ts0 = np.array([2.1,3.0,2.1,0,-2.1,-3,-2.1,0],dtype=np.float64)

linear = interpolate.interp1d(T0,Ts0,kind="linear",fill_value="extrapolate") # type: ignore
cubic = interpolate.interp1d(T0,Ts0,kind="cubic",fill_value="extrapolate") # type: ignore
nearest = interpolate.interp1d(T0,Ts0,kind="nearest",fill_value="extrapolate") # type: ignore

T = np.linspace(1,24,24)
Ts_linear = linear(T)
Ts_cubic = cubic(T)
Ts_nearest = nearest(T)

plt.plot(T,Ts_linear)
plt.plot(T,Ts_cubic)
plt.plot(T,Ts_nearest)
plt.plot(T0,Ts0,"o")
plt.show()