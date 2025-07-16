import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read multiple days' data from CSV
df = pd.read_csv("data_multi.csv")
time = df['time']

colors = ['red', 'green', 'blue']
days = ['day1', 'day2', 'day3']

for i in range(3):
    temp = df[days[i]]
    coeffs = np.polyfit(time, temp, 2)
    a, b, c = coeffs
    x = np.linspace(min(time), max(time), 200)
    y = a * x**2 + b * x + c

    plt.plot(x, y, color=colors[i], label=f'Day {i+1} Curve')
    plt.scatter(time, temp, color=colors[i], s=50, label=f'Day {i+1} Data')

plt.title("Temperature vs Time for 3 Days")
plt.xlabel("Time (Hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("exp1_stage4_graph.png")
plt.show()
