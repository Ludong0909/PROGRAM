import numpy as np
import matplotlib.pyplot as plt
import Cheers

# Constants
L = 5e3  # Length in m
H = 1e3  # Height in m
u = 5  # wind flow rate in m/s
Cin = 5  # Concentration in wind in kg/m^3
Eu = 128  # kg/m^2s
Er = 1  # kg/m^2s

# Time parameters
dt = 1  # Time step
t_total = 50000  # Total time
num_steps = int(t_total / dt) + 1

# Initial concentrations
Cu_initial = 0  # Initial concentration in upper layer
Cr_initial = 0  # Initial concentration in lower layer

# Arrays to store concentrations
t = np.linspace(0,50000,num_steps)
Cu = np.zeros(num_steps)
Cr = np.zeros(num_steps)
Analytical_Cu = 133
Analytical_Cr = 134

# Functions
def dCu_dt(t, Cu, Cr):
    return u*Cin/L + Eu/H - u*Cu/L


def dCr_dt(t, Cu, Cr):
    return u*Cu/L + Er/H - u*Cr/L

for Eu  in [128,64,32,16,8]:

    # Functions
    def dCu_dt(t, Cu, Cr):
        return u*Cin/L + Eu/H - u*Cu/L


    def dCr_dt(t, Cu, Cr):
        return u*Cu/L + Er/H - u*Cr/L

    # RK4 integration
    t, Cu, Cr = Cheers.ODE2_RK4(t, 0, 0, dCu_dt, dCr_dt, 1)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(t, Cu)
    plt.plot(t, Cr)
    plt.xlabel('Time (s)')
    plt.ylabel('Concentration (kg/m^3)')
    plt.title('Concentration vs Time')
    plt.legend(['Cu', 'Cr'])
    plt.grid()
    plt.savefig(f'Eu = {Eu}.png')
    plt.show()
