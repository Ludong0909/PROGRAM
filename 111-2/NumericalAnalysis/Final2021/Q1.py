import numpy as np
import matplotlib.pyplot as plt

D = 1
dt = 5e-5
dx = 0.02
T = 0.05
Nx = int(1 / dx) + 1  # 51
Nt = int(T / dt) + 1  # 1001

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
        
        u[i, j + 1] = u[i, j] + D * (dt / dx ** 2) * (right_neighbor - 2 * u[i, j] + left_neighbor)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, u[:, 0], label='t=1')
plt.plot(x, u[:, 99], label='t=100')
plt.plot(x, u[:, 299], label='t=300')
plt.plot(x, u[:, 599], label='t=600')
plt.plot(x, u[:, 999], label='t=1000')
plt.xlabel('x')
plt.ylabel('u')
plt.ylim(0,)
plt.title('Distribution of u')
plt.savefig('Diffusion.png', dpi=500)
plt.legend()
plt.show()
