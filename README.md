# Logistic Map, Lorenz Attractor, and Phase Diagram with Two Trajectories

## Logistic Map

### Overview
The logistic map is a classic example of how complex, chaotic behavior can arise from simple nonlinear dynamical equations. It is defined by the following recurrence relation:

\[ x_{n+1} = r x_n (1 - x_n) \]

where \(x_n\) is the state of the system at iteration \(n\), and \(r\) is a parameter that controls the dynamics of the system.

### Script Explanation
1. **Initialization:**
   - Set the parameter \(r\) to a value within the range where chaotic behavior is observed (e.g., 3.9).
   - Initialize the starting value \(x_0\) in the interval \([0, 1]\).
   - Define the number of iterations to run the map.

2. **Iteration:**
   - Compute \(x_{n+1}\) for each iteration using the logistic map formula.
   - Store or plot the resulting sequence of \(x_n\) values to visualize the behavior.

3. **Visualization:**
   - Plot \(x_n\) against \(n\) to observe how the values evolve over time.
   - Use a bifurcation diagram to illustrate the changes in behavior as \(r\) is varied.

## Lorenz Attractor

### Overview
The Lorenz attractor is a system of ordinary differential equations originally developed to model atmospheric convection. It is given by:

\[
\begin{align*}
\frac{dx}{dt} &= \sigma (y - x) \\
\frac{dy}{dt} &= x (\rho - z) - y \\
\frac{dz}{dt} &= x y - \beta z
\end{align*}
\]

where \(\sigma\), \(\rho\), and \(\beta\) are system parameters.

### Script Explanation
1. **Initialization:**
   - Set the parameters \(\sigma\), \(\rho\), and \(\beta\) to their standard values (e.g., \(\sigma = 10\), \(\rho = 28\), \(\beta = 8/3\)).
   - Define the initial conditions for \(x\), \(y\), and \(z\).

2. **Numerical Integration:**
   - Use a numerical method (such as Runge-Kutta) to solve the differential equations over a specified time range.
   - Integrate the equations to compute the trajectories of \(x(t)\), \(y(t)\), and \(z(t)\).

3. **Visualization:**
   - Plot the 3D trajectory of the Lorenz attractor in the \(x\)-\(y\)-\(z\) space.
   - This plot reveals the chaotic nature of the system and the characteristic butterfly shape.

## Phase Diagram with Two Trajectories

### Overview
A phase diagram provides insight into the behavior of a system by plotting trajectories in its phase space. For the logistic map or Lorenz attractor, this involves plotting the state variables against each other.

### Script Explanation
1. **Initialization:**
   - Set up the parameters and initial conditions for the two trajectories to be plotted.

2. **Trajectory Calculation:**
   - For the logistic map, compute \(x_n\) for two different initial conditions and parameters.
   - For the Lorenz attractor, integrate the system equations for two different sets of initial conditions.

3. **Visualization:**
   - For the logistic map, plot \(x_n\) against \(x_{n+1}\) to show the phase space structure.
   - For the Lorenz attractor, plot \(x\) against \(y\) or \(x\) against \(z\) to visualize the attractor’s shape.
   - Overlay the trajectories of the two initial conditions to compare their evolution and highlight differences.
