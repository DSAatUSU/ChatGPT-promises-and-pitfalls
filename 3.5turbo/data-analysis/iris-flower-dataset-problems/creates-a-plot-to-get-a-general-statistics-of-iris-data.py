import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset from a CSV file
iris_data = pd.read_csv('iris.csv')

# Get the column names
column_names = iris_data.columns

# Calculate the mean for each feature
means = iris_data.mean()

# Calculate the standard deviation for each feature
stds = iris_data.std()

# Create a bar plot for the mean values
plt.figure(figsize=(10, 6))
plt.bar(column_names[:-1], means[:-1])
plt.xlabel('Features')
plt.ylabel('Mean')
plt.title('Mean Values of Iris Dataset Features')
plt.show()

# Create a bar plot for the standard deviation values
plt.figure(figsize=(10, 6))
plt.bar(column_names[:-1], stds[:-1])
plt.xlabel('Features')
plt.ylabel('Standard Deviation')
plt.title('Standard Deviation of Iris Dataset Features')
plt.show()
