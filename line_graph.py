import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create line graph
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Add title and labels
plt.title("Line Graph Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display grid
plt.grid(True)

# Show graph
plt.show()
