import matplotlib.pyplot as plt
import numpy as np

# Data for time and displacement
time = [0, 0.25, 0.50, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
displacement = [0, 0.60, 1.20, 1.8, 2.4, 3.0, 3.6, 4.2, 4.8]

# Calculate the slope and intercept using numpy's polyfit function
slope, intercept = np.polyfit(time, displacement, 1)

# Output the slope
print("Slope of the line:", slope)

# Calculate velocity for each time interval as the change in displacement over the change in time
velocities = [
    (displacement[i + 1] - displacement[i]) / (time[i + 1] - time[i])
    for i in range(len(time) - 1)
]

# Since velocities are calculated between intervals, plot them at the midpoint of each interval
time_midpoints = [(time[i] + time[i + 1]) / 2 for i in range(len(time) - 1)]

# Plotting displacement and velocity together
plt.figure(figsize=(8, 6))
plt.plot(
    time, displacement, marker="o", linestyle="-", color="b", label="Displacement (m)"
)
plt.plot(
    time_midpoints,
    velocities,
    marker="s",
    linestyle="--",
    color="r",
    label="Velocity (m/s)",
)
plt.xlabel("Time (seconds)")
plt.ylabel("Value")
plt.title("Displacement and Velocity vs. Time")
plt.legend()
plt.grid(True)
plt.show()
