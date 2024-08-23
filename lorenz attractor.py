import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Lorenz system parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Lorenz system equations
def lorenz(t, state):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Time points where the solution is computed
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Initial conditions
initial_state = [1.0, 1.0, 1.0]

# Solve the Lorenz system
sol = solve_ivp(lorenz, t_span, initial_state, t_eval=t_eval)

# Extract the solution
x = sol.y[0]
y = sol.y[1]
z = sol.y[2]

# Plot the Lorenz attractor
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5, color='b')
ax.set_title("Lorenz Attractor")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
plt.show()
