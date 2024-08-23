import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

n = 10000  
last = 1000  
r_values = np.linspace(3.84, 3.856, 1000) 
x = 1e-5 * np.ones(r_values.shape)  


plt.figure(figsize=(10, 6))

for i in range(n):
    x = logistic_map(r_values, x)
    
    if i >= (n - last):
        plt.plot(r_values, x, ',b', alpha=0.25)

plt.title("Logistic Map Bifurcation Diagram")
plt.xlabel("Growth Rate")
plt.ylabel("Population")
plt.xlim(3.84, 3.856)
plt.ylim(0.45, 0.55)
plt.show()
