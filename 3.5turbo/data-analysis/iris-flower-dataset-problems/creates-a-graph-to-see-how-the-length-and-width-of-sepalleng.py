import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris = pd.read_csv('iris.csv')

# Plot the distribution for SepalLength, SepalWidth, PetalLength, and PetalWidth
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot SepalLength distribution
axs[0, 0].hist(iris['SepalLength'], bins=20, color='skyblue')
axs[0, 0].set_title('Sepal Length Distribution')
axs[0, 0].set_xlabel('Sepal Length')
axs[0, 0].set_ylabel('Count')

# Plot SepalWidth distribution
axs[0, 1].hist(iris['SepalWidth'], bins=20, color='darkorange')
axs[0, 1].set_title('Sepal Width Distribution')
axs[0, 1].set_xlabel('Sepal Width')
axs[0, 1].set_ylabel('Count')

# Plot PetalLength distribution
axs[1, 0].hist(iris['PetalLength'], bins=20, color='limegreen')
axs[1, 0].set_title('Petal Length Distribution')
axs[1, 0].set_xlabel('Petal Length')
axs[1, 0].set_ylabel('Count')

# Plot PetalWidth distribution
axs[1, 1].hist(iris['PetalWidth'], bins=20, color='blueviolet')
axs[1, 1].set_title('Petal Width Distribution')
axs[1, 1].set_xlabel('Petal Width')
axs[1, 1].set_ylabel('Count')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
