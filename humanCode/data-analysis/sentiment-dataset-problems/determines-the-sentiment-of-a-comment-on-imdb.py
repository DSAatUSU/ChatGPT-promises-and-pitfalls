from transformers import pipeline
import pandas as pd

sentiment_pipeline = pipeline("sentiment-analysis")
data = pd.read_csv("../../tests_data/IMDBDataset.csv")
data_sentiments = data["sentiment"].tolist()
data_reviews = data["review"].tolist()

review = data_reviews[3]
print("IMDB Comment: ",review)
sentiment_prediction = sentiment_pipeline(review)
print("Sentiment: ",sentiment_prediction[0]['label'])
print("Score: ",sentiment_prediction[0]['score'])
