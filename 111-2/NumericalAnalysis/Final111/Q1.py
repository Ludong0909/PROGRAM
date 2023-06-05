import numpy as np
import matplotlib.pyplot as plt

C = 0.5  # speed
dt = 0.01
dx = 0.025
Nx = int(1 / dx) + 1  # 51
Nt = int(2 / dt) + 1  # 1001

# Initialize grid
u = np.zeros((Nx, Nt))
x = np.linspace(0, 1, Nx)
u[:, 0] = np.exp(-((x - 0.5) ** 2) / (2 * (0.05 ** 2))) / np.sqrt(2 * np.pi * (0.05 ** 2))

# Apply finite difference method with periodic boundary condition
for j in range(Nt - 1):
    for i in range(Nx):
        # Add periodic boundary conditions
        left_neighbor = u[(i - 1) % Nx, j]
        right_neighbor = u[(i + 1) % Nx, j]
        
        u[i, j + 1] = u[i, j] + C * (dt / dx / 2) * (right_neighbor - left_neighbor)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, u[:, 0], label='t=0')
plt.plot(x, u[:, 19], label='t=20')
plt.plot(x, u[:, 39], label='t=40')
plt.plot(x, u[:, 59], label='t=60')
plt.plot(x, u[:, 79], label='t=80')
plt.plot(x, u[:, 99], label='t=100')
plt.plot(x, u[:, 119], label='t=120')
plt.xlabel('x')
plt.ylabel('u')
plt.ylim(0,)
plt.xlim(0,1)
plt.title('Distribution of u')
plt.savefig('Advection(c1).png', dpi=500)
plt.legend(loc = 'best')
plt.show()