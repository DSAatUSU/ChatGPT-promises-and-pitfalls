import pandas as pd

# Load the iris dataset from a CSV file
data = pd.read_csv("iris.csv")

# Calculate and display the statistical details
stat_details = data.describe()
print(stat_details)