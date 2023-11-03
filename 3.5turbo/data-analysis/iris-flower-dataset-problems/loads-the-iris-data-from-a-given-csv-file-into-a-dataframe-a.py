import pandas as pd

# Load the iris data from csv file into a dataframe
iris_data = pd.read_csv("iris.csv")

# Print the shape of the data
print("Shape of the data:", iris_data.shape)

# Print the type of the data
print("Type of the data:", type(iris_data))

# Print the first 3 rows of the data
print("First 3 rows of the data:")
print(iris_data.head(3))