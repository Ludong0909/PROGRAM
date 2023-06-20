'''
NA Functions for the final

by Zhiran
'''
import numpy as np
import matplotlib.pyplot as plt
import NAFunc as cheers
'''
Difference Formula
For def function
'''
# Two point central difference formula
def df_2c(f,x1,x2):
    '''
    2p CDF at x
    x1 < x < x2
    '''
    df = (f(x2)-f(x1))/(2*(x2-x1)/2)
    return df

# Four point central difference formula
def df_4c(f,x1,x2,x3,x4):
    '''
    4p CDF at x
    x1<x2<x<x3<x4
    '''
    df = (f(x1)-8*f(x2)+8*f(x3)-f(x4))/(12*(x3-x2)/2)
    return df

'''
For array
'''
# First derivative
# Two-point central difference
# with 3p Forward at the begin, 3p backward at the end
def dYdX_2c(X,Y):
    dYdX = np.zeros(len(X))
    # 3p Forward
    dYdX[0] = (-3*Y[0]+4*Y[1]-Y[2])/(2*(X[1]-X[0]))
    # 2p Central
    for i in range(1,len(X)-1):
        dYdX[i] = (Y[i+1]-Y[i-1])/(2*(X[i]-X[i-1]))
    # 3p Backward
    dYdX[-1] = (Y[-3]-4*Y[-2]+3*Y[-1])/(2*(X[-1]-X[-2]))
    return dYdX

# Second Derivative
# Three-point central difference
# with 4p Forward at the begin, 4p backward at the end
def ddYdXX_3c(X,Y):
    ddYdXX = np.zeros(len(X))
    # 4p Forward
    ddYdXX[0] = (2*Y[0]-5*Y[1]+4*Y[2]-Y[3])/((X[1]-X[0])**2)
    # 3p Central
    for i in range(1,len(X)-1):
        ddYdXX[i] = (Y[i-1]-2*Y[i]+Y[i+1])/((X[i]-X[i-1])**2)
    # 4p Backward
    ddYdXX[-1] = ((-Y[-4]+4*Y[-3]-5*Y[-2]+2*Y[-1])/((X[-1]-X[-2])**2))
    return ddYdXX

'''
ODE
用迴圈和前項迭代後項
'''
# Euler method
def Solve_Euler(x0,y0,func_ODE,h):
    def slope(x,y,func_ODE):
        return func_ODE(x,y)
    x1 = x0 + h
    y1 = y0 + slope(x0,y0,func_ODE)*h
    
    return x1,y1

# Modified Euler method
def Solve_ModEuler(x0,y0,func_ODE,h):
    def slope(x,y,func_ODE):
        return func_ODE(x,y)
    x1 = x0 + h
    y1 = y0 + slope(x0,y0,func_ODE)*h
    y1 = y0 + (slope(x0,y0,func_ODE)+slope(x1,y1,func_ODE))*h/2
    
    return x1,y1

# RK4 method
def Solve_RK4(x0,y0,func_ODE,h):
    def slope(x,y,func_ODE):
        return func_ODE(x,y)
    
    k1 = slope(x0,y0,func_ODE)
    x1 = x0 + h/2
    y1 = y0 + k1*h/2
    k2 = slope(x1,y1,func_ODE)
    x2 = x0 + h/2
    y2 = y0 + k2*h/2
    k3 = slope(x2,y2,func_ODE)
    x3 = x0 + h
    y3 = y0 + k3*h
    k4 = slope(x3,y3,func_ODE)

    x4 = x0 + h
    y4 = y0 + (k1+2*k2+2*k3+k4)*h/6
    
    return x4,y4

'''
ODE system
'''
def Slope(x, y, z, ODE_func):
    Slope = ODE_func(x,y,z)
    return Slope

# Euler explicit scheme
def ODE2_Euler(x, y_initial, z_initial, ODE_func1, ODE_func2, h):  # h for time step size (yr)

    y = np.zeros(len(x),dtype=float)
    z = np.zeros(len(x),dtype=float)

    y[0] = y_initial
    z[0] = z_initial

    for i in range(len(x)-1):
        x[i+1] = (x[i] + h)
        y[i+1] = (y[i] + h*Slope(x[i], y[i], z[i], ODE_func1))
        z[i+1] = (z[i] + h*ODE_func2(y,z))

    return x, y, z

# RK4 scheme
def ODE2_RK4(x, y_initial, z_initial, ODE_func1, ODE_func2, h):

    y = np.zeros(len(x),dtype=float)
    z = np.zeros(len(x),dtype=float)

    y[0] = y_initial
    z[0] = z_initial

    for i in range(len(x)-1):
        x[i+1] = x[i] + h
        sp1 = Slope(x[i], y[i], z[i], ODE_func1)
        sp12 = Slope(x[i], y[i], z[i], ODE_func2)

        sp2 = Slope(x[i] + 0.5*h, y[i] + 0.5*sp1*h, z[i] + 0.5*sp12*h, ODE_func1)
        sp22 = Slope(x[i] + 0.5*h, y[i] + 0.5*sp1*h, z[i] + 0.5*sp12*h, ODE_func2)

        sp3 = Slope(x[i] + 0.5*h, y[i] + 0.5*sp2*h, z[i] + 0.5*sp22*h, ODE_func1)
        sp32 = Slope(x[i] + 0.5*h, y[i] + 0.5*sp2*h, z[i] + 0.5*sp22*h, ODE_func2)

        sp4 = Slope(x[i] + h, y[i] + sp3*h, z[i] + sp32*h, ODE_func1)
        sp42 = Slope(x[i] + h, y[i] + sp3*h, z[i] + sp32*h, ODE_func2)

        y[i+1] = y[i] + h * (sp1 + 2*sp2 + 2*sp3 + sp4) / 6
        z[i+1] = z[i] + h * (sp12 + 2*sp22 + 2*sp32 + sp42) / 6

    return x, y, z

# n ODEs system
def ODEs_Solve_RK4(ODE_funcs, p0, vars, h):
    
    n = len(vars) # number of variables
    p = p0 # initial values of dependent variables

    # initialize arrays with zeros
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    k3 = np.zeros(n)
    k4 = np.zeros(n)
    v1 = np.zeros(n)
    v2 = np.zeros(n)
    v3 = np.zeros(n)
    v4 = np.zeros(n)

    for i in range(n):  # calculate k1 and v1 for each dependent variable
        k1[i] = ODE_funcs[i](p, *vars)
        v1[i] = vars[i] + k1[i] * h / 2

    p = p0 + h / 2  # update the value of the independent variable
    for i in range(n): 
        k2[i] = ODE_funcs[i](p, *v1) 
        v2[i] = vars[i] + k2[i] * h / 2 

    p = p0 + h / 2
    for i in range(n):
        k3[i] = ODE_funcs[i](p, *v2)
        v3[i] = vars[i] + k3[i] * h

    p = p0 + h
    for i in range(n):
        k4[i] = ODE_funcs[i](p, *v3)
        v4[i] = vars[i] + (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) * h / 6  # calculate the final value of the ith dependent variable using the weighted average of k1, k2, k3, and k4

    return p,tuple(v4)  # return the final values of the dependent variables as a tuple

'''
Integration
'''
# Trapezoidal method
def Trapz(f,Itv):
    I = 0
    for i in range(1,len(Itv)):
        I += (f(Itv[i-1])+f(Itv[i]))*(Itv[i]-Itv[i-1])/2
    return I


def Simpson13(f,Itv):
    if len(Itv) < 3 and len(Itv)%2==1:
        raise TypeError("Itv is too short!")
    I = 0
    for i in range(2,len(Itv),2):
        I += (f(Itv[i-2])+4*f(Itv[i-1])+f(Itv[i])) * (Itv[i]-Itv[i-2])/6
    return I

# Improper integral
def Trapz_improper(f,itv):
    ulimit = 1
    def Interval(ulimit):
        return np.linspace(0,ulimit,int(ulimit/itv))
    I = {1:Trapz(f,Interval(ulimit))}
    relativeDifference = 1
    while relativeDifference >= 1e-5:
        ulimit *= 2
        I[int(ulimit)] = Trapz(f,Interval(ulimit))
        relativeDifference = (I[ulimit]-I[ulimit/2])/I[ulimit/2]
    return I

'''
Temperature distribution
'''
def ODE_r2_c(V,dX,beta,Vs):
    n = len(V)-2
    A = np.zeros((n,n),dtype=np.float64)
    for i in range(n):
        for j in range(n):
            if i==j:
                A[i][j] = -(2+dX**2*beta)
            elif abs(i-j)==1:
                A[i][j] = 1
    AX = -(dX**2*beta*Vs)*np.ones(n,dtype=np.float64)
    AX[0] -= V[0]; AX[-1] -= V[-1]
    V[1:-1] = cheers.GaussElimination(A,AX)
    return V

def GaussSeidel_ODE(V,dX,beta,Vs,RHS):
    Vrel = np.ones(len(V))
    while(Vrel.any()>=1e-6):
        Vold = V.copy()
        factor = -(2+dX**2*beta)
        for i in range(1,len(V)-1):
            V[i] = (+RHS(V)[i]-(dX**2*beta*Vs)-V[i-1]-V[i+1])/factor
        Vnew = V.copy()
        Vrel = Vnew-Vold
    return V
    

def Div(u,v,nlon,nlat,r=6371e3):
    return 1/(r*2*np.pi)*(nlon*np.gradient(u)[0]+nlat*np.gradient(v)[1])

# fig, ax = plt.subplots(figsize=(12,6))
class quiverplot():
    def __init__(self,title=None) -> None:
        self.fig,self.axs = plt.subplots(figsize=(12,6))
        self.qvr = []
        self.title = title

    
    def quiver(self,u,v,nlon,nlat):
        self.lon = np.linspace(0,360,nlon);self.lat = np.linspace(-90,90,nlat)
        self.qvr.append(plt.quiver(self.lon,self.lat,u,v,width=0.001, headlength=3, headwidth=3))
        # plt.quiverkey(quiver2, 350, -88, 10, label='[m/s]')
        plt.xlim(0, 360)
        plt.ylim(-90, 90)
        plt.xticks(np.linspace(0, 360, 7))
        self.axs.set_xticklabels(['0E','60E','120E','180','120W','60W','0W'])
        plt.yticks(np.linspace(-90, 90, 7))
        self.axs.set_yticklabels(['90S','60S','30S','Equator','30N','60N','90N'])
        if self.title != None:
            plt.title("%s"%self.title)
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        return self
    
    def colormesh(self,F,nlon,nlat):
        import matplotlib.cm as cm
        self.lon = np.linspace(0,360,nlon);self.lat = np.linspace(-90,90,nlat)
        self.lon_grid, self.lat_grid = np.meshgrid(self.lon,self.lat)
        plt.pcolormesh(self.lon_grid,self.lat_grid,F,cmap=cm.RdBu,shading='gouraud')
        plt.colorbar(label='Divergence')
        return self