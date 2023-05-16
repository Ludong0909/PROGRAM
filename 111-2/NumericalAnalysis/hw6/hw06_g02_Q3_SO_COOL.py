import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

Time = np.array([3,6,9,12,15,18,21,24],dtype=float)
Ts = np.array([2.1,3.0,3.1,0,-2.1,-3,-2.1,0],dtype=float)

Time_whole = np.linspace(1,24,24)
Ts_whole = np.zeros(len(Time_whole))
Ts_whole[2], Ts_whole[5], Ts_whole[8], Ts_whole[11], Ts_whole[14], Ts_whole[17], Ts_whole[20], Ts_whole[23] = 2.1,3.0,2.1,0,-2.1,-3,-2.1,0
Ts_whole[np.where(Ts_whole==0)] = np.nan

plt.plot(Time_whole,Ts_whole,'o')

import numpy as np
from scipy.interpolate import interp1d

def interpolate_data(Time, Ts, kind='linear',length = 1000):
    """
    Perform linear interpolation on the given input data using SciPy's interp1d function.

    Args:
        Time (numpy.ndarray): Array of input time values.
        Ts (numpy.ndarray): Array of input Ts values corresponding to the time values.
        kind (str, optional): Type of interpolation. Default is 'linear'.
        length (int): The desired length of output array

    Returns:
        numpy.ndarray: Array of interpolated Ts values.
    """
    # Create an interpolation function using interp1d
    interpolator = interp1d(Time, Ts, kind=kind, fill_value='extrapolate')

    # Generate a new array of time values for interpolation
    new_time = np.linspace(0, 24, num=length)  # Modify num to change interpolation resolution

    # Perform interpolation using the interpolation function
    interpolated_Ts = interpolator(new_time)

    return interpolated_Ts

newTs = interpolate_data(Time, Ts, kind='nearest',length = len(Time))
plt.plot(Time,newTs)
plt.show()