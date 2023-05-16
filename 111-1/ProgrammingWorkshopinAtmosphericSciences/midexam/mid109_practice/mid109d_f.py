import numpy as np

def cal_cf (p,rh) :
    CF = (30+185*(1-p/1000))*np.exp((rh-100)/20)
    return CF

