import matplotlib.pyplot as plt

# Sample data
categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [150, 200, 180, 220, 170]     # For bar chart
profit = [50, 80, 60, 90, 70]         # For line chart

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(8,6))

# Bar chart for sales
ax1.bar(categories, sales, color='skyblue', label='Sales')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis for profit
ax2 = ax1.twinx()
ax2.plot(categories, profit, color='red', marker='o', linewidth=2, label='Profit')
ax2.set_ylabel('Profit', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add title and legends
plt.title('Sales and Profit Analysis')
fig.tight_layout()
plt.show()
