import pandas as pd
data = pd.read_csv("tests_data/iris.csv")
print('Iris-setosa')
setosa = data['Species'] == 'Iris-setosa'
print(data[setosa].describe())
print('\nIris-versicolor')
setosa = data['Species'] == 'Iris-versicolor'
print(data[setosa].describe())
print('\nIris-virginica')
setosa = data['Species'] == 'Iris-virginica'
print(data[setosa].describe())
