import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 4e6  # Surface area in m^2
h1 = 1  # Thickness of upper layer in m
h2 = 10  # Thickness of lower layer in m
Q = 12e6  # River flow rate in m^3/year
Ci = 1  # Concentration in river in mol/m^3
q = 12e4  # Exchange volume rate in m^3/year

# Time parameters
dt = 0.01  # Time step in years
t_total = 100  # Total time in years
num_steps = int(t_total / dt) + 1

# Initial concentrations
C1_initial = 0  # Initial concentration in upper layer
C2_initial = 0  # Initial concentration in lower layer

# Arrays to store concentrations
C1 = np.zeros(num_steps)
C2 = np.zeros(num_steps)
C1[0] = C1_initial
C2[0] = C2_initial

# Numerical integration using Euler Forward method
for i in range(1, num_steps):
    # Calculate time derivative at previous time step
    dC1_dt = (Q * Ci - Q * C1[i - 1]) / (A * h1) - (q * (C1[i - 1] - C2[i - 1])) / A
    dC2_dt = (q * (C1[i - 1] - C2[i - 1])) / A

    # Update concentrations using Euler Forward method
    C1[i] = C1[i - 1] + dt * dC1_dt
    C2[i] = C2[i - 1] + dt * dC2_dt

# Compute equilibrium concentrations at steady state
C1_eq = (Q * Ci + q * C2_initial) / (Q + q)
C2_eq = (Q * C1_eq) / Q

# Find the time it takes for C2 to drop to 1% of its equilibrium concentration
threshold = 0.01 * C2_eq
time_to_threshold = -1  # Initialize as -1 (not found)

for i in range(num_steps):
    if C2[i] <= threshold:
        time_to_threshold = i * dt
        break

# Print the results
print("Equilibrium Concentrations:")
print("C1_eq =", C1_eq)
print("C2_eq =", C2_eq)
print("Time to drop to 1% of equilibrium concentration:", time_to_threshold, "years")

# Plotting
t = np.linspace(0, t_total, num_steps)

plt.figure(figsize=(8, 6))
plt.plot(t, C1, label='Upper Layer')
plt.plot(t, C2, label='Lower Layer')
plt.xlabel('Time (years)')
plt.ylabel('Concentration (mol/m^3)')
plt.title('Concentration vs Time')
plt.legend()
plt.grid(True)
plt.show()


