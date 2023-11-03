import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("tests_data/iris.csv")
# Drop id column
new_data = iris.drop('Id',axis=1)
new_data.hist(edgecolor='black', linewidth=1.2)
fig=plt.gcf()
fig.set_size_inches(12,12)
plt.show()
