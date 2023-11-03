import numpy as np

def find_outliers(data):
    """
    Function to find outliers in a given data set
    Args:
    data: array-like or iterable, input data

    Returns:
    outliers: array, containing the outliers in the data set
    """
    # Convert the data to a numpy array for easy manipulation
    data = np.array(data)

    # Calculate the quartiles and interquartile range (IQR)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    # Calculate the lower and upper bounds for outliers detection
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    # Find the outliers
    outliers = data[(data < lower_bound) | (data > upper_bound)]

    return outliers

# Test the function
data = [1, 2, 3, 4, 5, 20, 21, 22, 23, 24, 50]
outliers = find_outliers(data)
print(outliers)
