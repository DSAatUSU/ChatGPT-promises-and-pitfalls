import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def get_sentiment(comment):
    # Initialize SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()

    # Get sentiment scores
    sentiment_scores = sia.polarity_scores(comment)

    # Determine sentiment label
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment

def main():
    # Get comment from user
    comment = input('Enter a comment: ')

    # Determine sentiment
    sentiment = get_sentiment(comment)

    # Print sentiment
    print('Sentiment:', sentiment)

if __name__ == '__main__':
    main()
