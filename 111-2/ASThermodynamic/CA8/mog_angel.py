# -*- coding: utf-8 -*-
"""
Created on Thu May 11 01:15:58 2023

@author: 安柔
"""

import numpy as np

A = 2.53e9
B = 5.42e3
p0 = 1000
Rd = 287
Cp = 1004
g = 9.8
Q = 0.03
R = 1.2e-4
Rv = 461
Rd = 287
Lv = 2.5e6
eps = 0.622

def es(T):
    return A * np.exp(-B / T)

def e(es, RH):
    return es * (RH * 0.01)

def qv(e, P):
    return (eps * e) / (P - (1 - eps) * e)

def qvs(T, P):
    return (eps * es(T)) / (P - (1 - eps) * es(T))

def Tv(qv, T):
    return (1 + 0.608*qv) * T

def theta(T, P):
    return T * ((p0 / P) ** (Rd / Cp))

def inv_theta(theta, P):
    return theta * ((P / p0) ** (Rd / Cp))

def Sd(T, H): 
    return Cp * T + g * H

def hm(T, H, qv):
    return Cp * T + g * H + Lv * qv

def hms(T, H, qvs):
    return Cp * T + g * H + Lv * qvs

def theta_e(theta, qv, T):
    return theta * np.exp(Lv * qv / (Cp * T))

def theta_l(theta, ql, T):
    return theta * np.exp(-Lv * ql / (Cp * T))

def dry_lapse(T, H1, H2):
        Tnew = T - (g / Cp) * (H1 - H2)
        return Tnew

def moist_lapse(T, H1, H2, qvs):
    Cps = Cp * ((1 + (Lv**2 * qvs) / (Cp * Rv * T**2))  /  (1 + (Lv * qvs) / (Rd * T)))
    Tnew = T - (g / Cps) * (H1 - H2)
    return Tnew

def CAPE(LFC, EL, H, p_qv, env_qv, p_T, env_T):
    def f(p_qv, p_T, env_qv, env_T):
        return g * (Tv(p_qv, p_T) - Tv(env_qv, env_T)) / Tv(env_qv, env_T)
    CAPE = np.trapz(f(p_qv[LFC:EL+1], p_T[LFC:EL+1], env_qv[LFC:EL+1], env_T[LFC:EL+1]), H[LFC:EL+1])
    return CAPE

def CIN(LFC, H, p_qv, env_qv, p_T, env_T):
    def f(p_qv, p_T, env_qv, env_T):
        return - g * (Tv(p_qv, p_T) - Tv(env_qv, env_T)) / Tv(env_qv, env_T)
    CIN = np.trapz(f(p_qv[:LFC+1], p_T[:LFC+1], env_qv[:LFC+1], env_T[:LFC+1]), H[:LFC+1])
    return CIN