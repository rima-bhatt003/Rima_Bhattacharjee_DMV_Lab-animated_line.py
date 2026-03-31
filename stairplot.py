import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Stair (step) plot
plt.step(x, y)

# Labels
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Stair Plot Example")

plt.show()