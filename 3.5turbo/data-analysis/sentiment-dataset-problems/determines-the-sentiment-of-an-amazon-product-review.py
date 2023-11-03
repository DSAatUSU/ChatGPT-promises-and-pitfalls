import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def get_review_sentiment(review):
    nltk.download('vader_lexicon')  # Download required dataset for SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(review)
    compound_score = sentiment_scores['compound']

    # Determine sentiment based on compound score
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Get user input for the Amazon product review
review = input("Enter your Amazon product review: ")

# Get the sentiment of the review
sentiment = get_review_sentiment(review)

# Output the sentiment
print(f"The sentiment of the review is: {sentiment}")
