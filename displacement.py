import matplotlib.pyplot as plt

# Data from Table 1
time = [0, 5, 10, 15, 20, 30, 35, 40, 45, 50]  # Time in seconds (x-axis)
position = [0, 20, 40, 50, 55, 60, 70, 70, 70, 55]  # Position in meters (y-axis)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(
    time,
    position,
    marker="o",
    linestyle="-",
    color="blue",
    label="Displacement over time",
)
plt.title("Position vs. Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Position (meters)")
plt.grid(True)
plt.legend()
plt.show()
