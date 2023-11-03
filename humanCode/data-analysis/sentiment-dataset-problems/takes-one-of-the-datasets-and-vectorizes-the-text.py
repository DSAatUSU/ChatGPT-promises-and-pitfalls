import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv("./humanCode/tests_data/IMDBDataset.csv")
data_sentiments = data["sentiment"].tolist()
data_reviews = data["review"].tolist()


review = data_reviews[0]
print("Example from dataset", review)

corpus = data_reviews
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
results = X.toarray()
print("Vectorized version of the Example: ", results[0])
