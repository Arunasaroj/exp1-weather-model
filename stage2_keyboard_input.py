import numpy as np
import matplotlib.pyplot as plt

# Directly assigned values (as if entered via keyboard)
time_values = [0, 2, 4, 6, 8, 9]
temperature_values = [30, 29, 33, 33, 28, 21]

# Fit quadratic curve
coeffs = np.polyfit(time_values, temperature_values, 2)
a, b, c = coeffs

x_smooth = np.linspace(min(time_values), max(time_values), 100)
y_smooth = a * x_smooth**2 + b * x_smooth + c

# Plotting
plt.plot(x_smooth, y_smooth, color='green', label='Temperature Curve')
plt.scatter(time_values, temperature_values, color='red', label='Data Points')
plt.title("Temperature vs Time (Keyboard Input - Auto Values)")
plt.xlabel("Time (Hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("exp1_stage2_graph.png")
plt.show()

