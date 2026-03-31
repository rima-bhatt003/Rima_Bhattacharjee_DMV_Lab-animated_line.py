import matplotlib.pyplot as plt

# Data
categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [25, 30, 20, 25]

# Create bar chart
plt.figure(figsize=(8,6))
plt.bar(categories, values, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Fruit Quantity Bar Chart')

# Show value on top of bars
for i, value in enumerate(values):
    plt.text(i, value + 0.5, str(value), ha='center')

plt.show()
