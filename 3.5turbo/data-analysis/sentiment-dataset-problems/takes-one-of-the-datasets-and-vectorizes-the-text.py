import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
dataset = pd.read_csv('dataset.csv')

# Extract the text data
text_data = dataset['text']

# Initialize the vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the text data
vectorized_data = vectorizer.fit_transform(text_data)

# Print the vectorized data
print(vectorized_data)
