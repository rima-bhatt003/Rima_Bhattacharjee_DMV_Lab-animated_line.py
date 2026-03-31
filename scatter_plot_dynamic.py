import matplotlib.pyplot as plt

# Ask user for X values
x_values = input("Enter X values separated by commas: ")
x = [float(i) for i in x_values.split(",")]

# Ask user for Y values
y_values = input("Enter Y values separated by commas: ")
y = [float(i) for i in y_values.split(",")]

# Check if lengths match
if len(x) != len(y):
    print("Error: Number of X and Y values must be the same!")
else:
    plt.scatter(x, y)
    plt.grid(True)  # Show grid
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Dynamic Scatter Plot")
    plt.show()


plt.show()
