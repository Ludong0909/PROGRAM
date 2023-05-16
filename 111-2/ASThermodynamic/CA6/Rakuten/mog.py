# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:43:59 2023

@author: USER
"""

import numpy as np

g = 9.8    # m/s**2
Rd = 287
Cp = 1004  # J/(K*kg)
Lv = 2.5e6 # J/kg
epsilon = 0.622
A = 2.53e9 # hPa
B = 5420   # K

def Tv(T, qv):
    return T * (1 + 0.608 * qv)

def theta(T, P):
    return(T * (1000 / P) ** (Rd / Cp))

def inv_theta(theta, P):
    return theta * (P / 1000) ** (Rd / Cp)

def Sd(T, H):
    return (Cp * T + g * H) / Cp

def buoyancy(Tv, Tv_env):
    return g * (Tv - Tv_env) / Tv

def qv(RH, T, P):
    es = A * np.exp(-B / T) # saturation pressure [hPa]
    e = es * RH / 100 # RH by [%]
    return epsilon * e / (P - (1 - epsilon) * e)

def qv_s(T, P):
    es = A * np.exp(-B / T)
    return epsilon * es / (P - (1 - epsilon) * es)

def theta_e(theta, qv, T):
    return theta * np.exp(Lv * qv / (Cp * T))

def theta_l(theta, ql, T):
    return theta * np.exp(-Lv * ql / (Cp * T))

def h_m_T(T, H, qv):
    return (Cp * T + g * H + Lv * qv) / Cp

def h_ms_T(T, H, P):
    return (Cp * T + g * H + Lv * qv_s(T, P)) / Cp