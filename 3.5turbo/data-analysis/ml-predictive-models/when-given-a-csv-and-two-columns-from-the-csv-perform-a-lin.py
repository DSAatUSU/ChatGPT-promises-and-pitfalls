import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('data.csv')

# Ask the user to input the names of two columns from the CSV
column1 = input('Enter the name of the first column: ')
column2 = input('Enter the name of the second column: ')

# Extract the specified columns from the DataFrame
X = df[column1].values.reshape(-1, 1)
y = df[column2].values

# Create an instance of LinearRegression
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Print the coefficients and intercept
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)

# Perform a prediction using the model
x_pred = float(input('Enter a value for {}: '.format(column1)))
y_pred = model.predict([[x_pred]])
print('Predicted {} for {}: {}'.format(column2, column1, y_pred[0]))
