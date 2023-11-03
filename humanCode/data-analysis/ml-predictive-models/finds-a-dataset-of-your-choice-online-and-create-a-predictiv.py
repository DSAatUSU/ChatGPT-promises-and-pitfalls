# 2. Import libraries and modules
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# 3. Load red wine data.
dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(dataset_url, sep=";")

# 4. Split data into training and test sets
y = data.quality
X = data.drop("quality", axis=1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123, stratify=y
)

# 5. Declare data preprocessing steps
pipeline = make_pipeline(
    preprocessing.StandardScaler(),
    RandomForestRegressor(n_estimators=100, random_state=123),
)

# 6. Declare hyperparameters to tune
hyperparameters = {
    "randomforestregressor__max_features": ["auto", "sqrt", "log2"],
    "randomforestregressor__max_depth": [None, 5, 3, 1],
}

# 7. Tune model using cross-validation pipeline
clf = GridSearchCV(pipeline, hyperparameters, cv=10)

clf.fit(X_train, y_train)

# 8. Refit on the entire training set
# No additional code needed if clf.refit == True (default is True)

# 9. Evaluate model pipeline on test data
pred = clf.predict(X_test)
print(r2_score(y_test, pred))
print(mean_squared_error(y_test, pred))

# 10. Save model for future use
joblib.dump(clf, "rf_regressor.pkl")
# To load: clf2 = joblib.load('rf_regressor.pkl')
