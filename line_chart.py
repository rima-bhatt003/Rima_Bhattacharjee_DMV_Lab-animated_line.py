import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

# Create line chart
plt.figure()
plt.plot(x, y)

# Add labels and title
plt.title("Simple Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot
plt.show()
