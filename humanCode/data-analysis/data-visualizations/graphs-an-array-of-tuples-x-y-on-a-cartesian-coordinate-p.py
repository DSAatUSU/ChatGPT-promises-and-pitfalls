import pandas as pd
import matplotlib.pyplot as plt

tuples = [(2, 4), (1, -6), (-4, 2), (-3, -7), (0, 0), (1, 2), (-2, -1), (-3, -1), (-1, -4)]

df = pd.DataFrame(tuples, columns=['xVal', 'yVal'])
df.plot(kind='scatter', x='xVal', y='yVal')
plt.show()
