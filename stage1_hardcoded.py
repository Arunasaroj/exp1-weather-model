import numpy as np
import matplotlib.pyplot as plt

time_values = np.array([0, 2, 4, 6, 8, 10])
temperature_values = np.array([20, 25, 30, 28, 25, 20])

coeffs = np.polyfit(time_values, temperature_values, 2)
a, b, c = coeffs

x_smooth = np.linspace(0, 10, 100)
y_smooth = a * x_smooth**2 + b * x_smooth + c

plt.plot(x_smooth, y_smooth, color='blue', label='Temperature Curve')
plt.scatter(time_values, temperature_values, color='red', label='Data Points')
plt.title("Temperature vs Time (Hardcoded Values)")
plt.xlabel("Time (Hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("exp1_stage1_graph.png")
plt.show()
