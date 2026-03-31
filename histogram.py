import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.randn(1000)

# Create histogram
plt.figure()
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Add title and labels
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show plot
plt.show()
