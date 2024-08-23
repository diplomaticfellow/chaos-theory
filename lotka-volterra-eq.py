import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def lotka_volterra(t, z, alpha, beta, delta, gamma):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]


alpha = 1.0  
beta = 0.1  
delta = 0.075  
gamma = 1.5


initial_conditions = [[0.7, 3], [2, 6]]


t_span = [0, 50]
t_eval = np.linspace(t_span[0], t_span[1], 1000)

plt.figure(figsize=(10, 8))

for x0, y0 in initial_conditions:
    sol = solve_ivp(lotka_volterra, t_span, [x0, y0], args=(alpha, beta, delta, gamma), t_eval=t_eval)
    plt.plot(sol.y[0], sol.y[1], label=f'x0={x0}, y0={y0}')

x = np.linspace(0, 3, 100)
y1 = alpha / beta 
y2 = gamma / delta * (1 / x)  
plt.plot(x, y1 * np.ones_like(x), 'g', label='dx/dt=0')
plt.plot(x, y2, 'y', label='dy/dt=0')

plt.title("Phase diagram with two trajectories")
plt.xlabel("Prey population")
plt.ylabel("Predator population")
plt.legend()
plt.grid()
plt.show()
