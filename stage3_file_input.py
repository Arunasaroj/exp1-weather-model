import numpy as np
import matplotlib.pyplot as plt

# Read time and temperature values from file
with open("data.txt", "r") as f:
    time_values = list(map(float, f.readline().strip().split(',')))
    temp_values = list(map(float, f.readline().strip().split(',')))

# Fit quadratic curve
coeffs = np.polyfit(time_values, temp_values, 2)
a, b, c = coeffs

# Generate smooth curve
x_smooth = np.linspace(min(time_values), max(time_values), 200)
y_smooth = a * x_smooth**2 + b * x_smooth + c

# Plotting
plt.plot(x_smooth, y_smooth, color='purple', label='Temperature Curve')
plt.scatter(time_values, temp_values, color='orange', label='Data Points')
plt.title("Temperature vs Time (File Input)")
plt.xlabel("Time (Hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("exp1_stage3_graph.png")
plt.show()
