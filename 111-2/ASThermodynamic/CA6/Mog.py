import numpy as np
import sympy as sym

Rd = 287  # gas const for dry air [J/K*kg]
Cp = 1004  # specific heat capacity of air [J/K*kg]
Rv = 461  # gas const for vapor [J/K*kg]
Lv = 2.5e6  # evaporating latent heat [J/kg]
g0 = 9.80665  # gravity acceleration [m/s^2]
epsilon = Rd / Rv

# Empirical Constant for C.C. equation
A = 2.53*10**9  # [hPa]
B = 5.42*10**3  # [K]


def PotentialTemp (T, P):  # theta
    """
    Args:
        T: Temperature [K]
        P: Pressure [hPa][mb]
    
    Returns:
        theta: Potential Temperature [K]
    """
    P0 = 1000 #pressure [hPa]
    Rd = 287 #gas const for dry air [J/K*kg]
    Cp = 1004 #specific heat capacity of air [J/K*kg]

    theata = T*((P0/P)**(Rd/Cp)) #[K]

    return(theata)


def SaturationWaterVaporPressure (T):  # es
    """
    Using C.C. equation to calculate es.

    Args:
        T: Temperature [K]
    
    Returns:
        es: saturation water vapor pressure [mb]
    """
    A = 2.53*10**9  # hPa
    B = 5.42*10**3  # K

    es = A*np.exp(-B/T)

    return(es) 


def SpecificHumidity (P, e):  # qv
    """
    Args:
        P: Pressure [hPa]
        e: water vapor pressure [hPa][mb]
    
    Returns:
        qv: specific humidity [kg/kg]
    """
    Rd = 287 #[J/K*kg]
    Rv = 461 #[J/K*kg]
    epsilon = Rd/Rv

    qv = epsilon*e/(P-(1-epsilon)*e)

    return(qv)


def VirtualTemp(T, qv):  # Tv
    """
    Args:
        T: Temperature [K]
        qv: specific humidity [kg/kg]
    
    Returns:
        Tv: virtual temperature [K]
    """    
    Rd = 287 #[J/K*kg]
    Rv = 461 #[J/K*kg]
    epsilon = Rd/Rv

    Tv = (1+epsilon*qv)*T

    return(Tv)


def VirtualPotentialTemp (T, qv, P):  # theta_v
    """
    Args:
        T: Temperature [K]
        qv: specific humidity [kg/kg]
        P: pressure [hPa][mb]
    
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
        P1: pressure at top [hPa][mb]
        P2: pressure at base [hPa][mb]
        Tv_ave: average virtual temperature [K]
    
    Returns:
        delta_z: height between two pressure level [m]
    """   
    g0 = 9.80665  # [m/s^2]
    Rd = 287  # [J/K*kg]

    delta_Z = ((Rd * Tv_ave)/g0) * np.log((P1/P2))

    return delta_Z


def DryStaticEnergy (T, H):  # Sd
    """
    Args:
        T: Temperature [K]
        H: Height [m]

    Returns:
        Sd: dry static energy [J]
    """ 
    Cp = 1004
    g0 = 9.80665

    Sd = Cp * T + g0 * H 

    return Sd


def MoistStaticEnergy (T, H, qv):  # hm
    """
    If substitute qv as qvs, get saturation moist static energy (hms).

    Args:
        T: Temperature [K]
        H: Height [m]
        qv: specific humidity [kg/kg]

    Returns:
        hm: moist static energy [J]
    """

    hm = Cp * T + g0 * H + Lv * qv

    return hm


def Buoyancy(Tv, Tv_env):  # B
    """
    Args:
        Tv: Virtual Temperature [K]
        H: Height [m]
        qv: Specific Humidity [kg/kg]
    
    Returns:
        Bouyancy: Bouyancy of parcel [m/s^2]
    """

    return g0 * (Tv - Tv_env) / Tv


def SpecificHumidity_RH(RH, T, P):  # qv, using RH
    """
    Args:
        RH: Relative Humidity [%] 
        T: Temperature [K]
        P: Pressure [hPa][mb]
    
    Returns:
        qv: Specific Humidity [kg/kg]
    """
    es = A * np.exp(-B / T) # saturation pressure [hPa]
    e = es * RH / 100 # RH by [%]
    return epsilon * e / (P - (1 - epsilon) * e)


def SaturatedSpecificHumidity(T, P):  # qvs
    """
    Args:
        T: Temperature [K]
        P: Pressure [hPa][mb]
    
    Returns:
        qv: specific humidity [kg/kg]
    """
    es = A * np.exp(-B / T)  # Saturated Vapor Pressure
    return epsilon * es / (P - (1 - epsilon) * es)


def EquivalentPotentialTemp(theta, qv, T):  #theta_e
    """
    Args:
        theta: Potential Temperature [K]
        qv: Specific Humidity [kg/kg]
    
    Returns:
        theta_e: Equivalent Potential Temperature [K]
    """

    theta_e = theta * np.exp(Lv * qv / (Cp * T))

    return theta_e


def EquivalentLiquidPotentialTemp(theta, ql, T):  # theta_l
    """
    Args:
        theta: Potential Temperature [K]
        ql: Specific Humidity of Liquid [kg/kg]
        T: Temperature [K]
    
    Returns:
        theta_l: Equivalent Liquid Potential Temperature [K]
    """

    theta_l = theta * np.exp(-Lv * ql / (Cp * T))

    return theta_l 


def SaturatedMoistStaticEnergy(T, H, P):  #hms
    """
    Args:
        T: Temperature [K]
        H: Height [m]
        P: Pressure [hPa][mb]

    Returns:
        hms: Saturated moist static energy [J]
    """

    hms =  (Cp * T + g0 * H + Lv * SaturatedSpecificHumidity(T, P))

    return hms
