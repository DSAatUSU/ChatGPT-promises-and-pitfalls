import pandas as pd

# Import iris data from csv file into a dataframe
from sklearn.datasets import load_iris

if __name__ == "__main__":
    data = load_iris()
    # data = pd.read_csv("iris.csv")
    print("Shape of the data:")
    print(data.shape)
    print("\nData Type:")
    print(type(data))
    print("\nFirst 3 rows:")
    print(data.head(3))
