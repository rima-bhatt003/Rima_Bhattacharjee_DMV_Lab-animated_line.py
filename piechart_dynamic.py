import matplotlib.pyplot as plt
from  import interact, widgets

# Function to plot pie chart
def plot_pie(label1, value1, label2, value2, label3, value3):
    labels = [label1, label2, label3]
    sizes = [value1, value2, value3]
    explode = [0.05]*3  # Slightly pop out all slicesp
    
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    plt.show()

# Interactive widget
interact(plot_pie,
         label1=widgets.Text(value='Apples', description='Label 1:'),
         value1=widgets.FloatSlider(value=30, min=0, max=100, description='Value 1:'),
         label2=widgets.Text(value='Bananas', description='Label 2:'),
         value2=widgets.FloatSlider(value=40, min=0, max=100, description='Value 2:'),
         label3=widgets.Text(value='Cherries', description='Label 3:'),
         value3=widgets.FloatSlider(value=30, min=0, max=100, description='Value 3:')
        )
