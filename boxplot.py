import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('iris.csv', header=None)

# Assign column names
df.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Class']

# ---- Fix incorrect class labels ----
# Replace wrong entries with proper species names
df['Class'] = df['Class'].replace({
    'petal': 'versicolor',   # wrong → correct
    'setosa ': 'setosa',     # remove trailing space
    'virginica ': 'virginica'
})

# Convert numeric columns
for col in df.columns[:-1]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop invalid rows
df = df.dropna()

# ---- Check all class names ----
print("Classes in dataset:", df['Class'].unique())

# ---- Boxplot grouped by all species ----
df.boxplot(by='Class', figsize=(10, 6))

plt.suptitle("")
plt.title("Boxplot of All Iris Species")
plt.xlabel("Species (setosa, versicolor, virginica)")
plt.ylabel("Values")

plt.show()
