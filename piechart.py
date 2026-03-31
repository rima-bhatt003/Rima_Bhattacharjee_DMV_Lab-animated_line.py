import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 10, 40, 25]  # Percentage or counts
colors = ["#ce0c0c","#2874c0","#0b570b","#b97026"]
explode = (0.05, 0.05, 0.05, 0.05)  # "explode" all slices slightly

# Create pie chart
plt.figure(figsize=(6,6))  # Set figure size
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', startangle=90, shadow=True)

plt.title("Fruit Distribution")
plt.axis('equal')  # Equal aspect ratio ensures pie is circular
plt.show()
