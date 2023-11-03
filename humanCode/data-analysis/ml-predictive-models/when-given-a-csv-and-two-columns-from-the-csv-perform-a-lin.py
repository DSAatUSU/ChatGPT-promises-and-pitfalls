# Step 1: Import packages and classes
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

# Import Example dataset for simple regression problem
from sklearn.datasets import make_regression

# Step 2: Provide data
x, y = make_regression(n_samples=8, n_features=1, noise=10)

x, y = np.array(x), np.array(y)

# Step 2b: Transform input data
x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)

# Step 3: Create a model and fit it
model = LinearRegression().fit(x_, y)

# Step 4: Get results
r_sq = model.score(x_, y)
intercept, coefficients = model.intercept_, model.coef_

# Step 5: Predict response
y_pred = model.predict(x_)
