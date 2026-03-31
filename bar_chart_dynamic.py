import matplotlib.pyplot as plt

# Ask user for number of bars
n = int(input("Enter the number of categories: "))

categories = []
values = []

# Take category names and values from user
for i in range(n):
    category = input(f"Enter name for category {i+1}: ")
    value = float(input(f"Enter value for {category}: "))
    categories.append(category)
    values.append(value)

# Create bar chart
plt.figure(figsize=(8,6))
plt.bar(categories, values, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Dynamic Bar Chart')

# Show value on top of bars
for i, value in enumerate(values):
    plt.text(i, value + 0.5, str(value), ha='center')

plt.show()
