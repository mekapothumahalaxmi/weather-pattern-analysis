import matplotlib.pyplot as plt

# Weather data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [30, 32, 31, 29, 28, 33, 35]

# Create line chart
plt.plot(days, temperature, marker='o')

# Chart title and labels
plt.title("Weather Pattern Analysis")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

# Show grid
plt.grid(True)

# Display chart
plt.show()