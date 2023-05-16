import numpy as np
import sympy as sym

Rd = 287  # gas const for dry air [J/K*kg]
Cp = 1004  # specific heat capacity of air [J/K*kg]
Rv = 461  # [J/K*kg]


def PotentialTemp (T, P):
    """
    Args:
        T: Temperature
        P: Pressure
    
    Returns:
        Potential Temperature [K]
    """
    P0 = 1000 #pressure [hPa]
    Rd = 287 #gas const for dry air [J/K*kg]
    Cp = 1004 #specific heat capacity of air [J/K*kg]

    theata = T*((P0/P)**(Rd/Cp)) #[K]

    return(theata)

def SaturationWaterVaporPressure (T):
    """
    Args:
        T: Temperature [K]
    
    Returns:
        es: saturation water vapor pressure [mb]
    """
    A = 2.53*10**9  # hPa
    B = 5.42*10**3  # K

    es = A*np.exp(-B/T)

    return(es) 

def SpecificHumidity (P, e):
    """
    Args:
        P: Pressure
        e: water vapor pressure
    
    Returns:
        qv: specific humidity [kg/kg]
    """
    Rd = 287 #[J/K*kg]
    Rv = 461 #[J/K*kg]
    epsilon = Rd/Rv

    qv = epsilon*e/(P-(1-epsilon)*e)

    return(qv)

def VirtualTemp(T, qv):
    """
    Args:
        T: Temperature
        qv: specific humidity
    
    Returns:
        Tv: virtual temperature [K]
    """    
    Rd = 287 #[J/K*kg]
    Rv = 461 #[J/K*kg]
    epsilon = Rd/Rv

    Tv = (1+epsilon*qv)*T

    return(Tv)

def VirtualPotentialTemp (T, qv, P):
    """
    Args:
        T: Temperature
        qv: specific humidity
        P: pressure
    
    Returns:
        theta_v: virtual potential temperature [K]
    """ 
    P0 = 1000  #[hPa]
    Rd = 287  #[J/K*kg]
    Cp = 1004  #[J/*K*kg]
    theta_v = T * (1 + 0.608*qv) * (P0/P)**(Rd/Cp)

    return theta_v

def HypsometricEquation (P1, P2, Tv_ave):
    """
    Args:
        P1: pressure at top
        P2: pressure at base
        Tv_ave: average virtual temperature
    
    Returns:
        delta_z: height between two pressure level [m]
    """   
    g0 = 9.80665  # [m/s^2]
    Rd = 287  # [J/K*kg]

    delta_Z = ((Rd * Tv_ave)/g0) * np.log((P1/P2))

    return delta_Z

def SmoothData (data, window_size):
    """
    Assisted by ChatGPT
    Compute a moving average of a given dataset with a specified window size.

    Args:
        data (list): A list of numbers to be smoothed.
        window_size (int): The number of data points to include in the moving window.

    Returns:
        list: A list of smoothed values, where each value is the average of the `window_size` adjacent values in the original dataset.

    """
    half_window = (window_size - 1) // 2
    smoothed_data = []
    for i in range(len(data)):
        if i < half_window:
            # Not enough data points to compute a full window on the left
            smoothed_data.append(data[i])
        elif i >= len(data) - half_window:
            # Not enough data points to compute a full window on the right
            smoothed_data.append(data[i])
        else:
            # Compute the average of the window
            window_sum = sum(data[i - half_window:i + half_window + 1])
            window_average = window_sum / window_size
            smoothed_data.append(window_average)
    return smoothed_data

def DryStaticEnergy (T, H):
    """
    Args:
        T: Temperature
        H: Height    

    Returns:
        Sd: dry static energy [J]
    """ 
    Cp = 1004
    g0 = 9.80665

    Sd = Cp * T + g0 * H 

    return Sd