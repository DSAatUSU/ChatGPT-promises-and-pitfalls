import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("tests_data/iris.csv")
iris.describe().plot(kind = "area",fontsize=16, figsize = (15,8), table = True, colormap="Accent")
plt.xlabel('Statistics',)
plt.ylabel('Value')
plt.title("General Statistics of Iris Dataset")
plt.show()
