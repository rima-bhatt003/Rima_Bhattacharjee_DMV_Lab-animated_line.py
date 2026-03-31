import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 1, 5, 3, 6]

# Create scatter plot
plt.figure()
plt.scatter(x, y, color='red', marker='o')

# Add title and labels
plt.title("Static Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add grid
plt.grid(True)

# Show plot
plt.show()
