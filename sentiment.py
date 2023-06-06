from nltk.sentiment import SentimentIntensityAnalyzer


def analyze(text):
    # Step 1: Initialize the sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Step 2: Perform sentiment analysis on the text
    sentiment_scores = sid.polarity_scores(text)

    # Step 3: Interpret the sentiment scores
    compound_score = sentiment_scores["compound"]
    if compound_score >= 0.05:
        sentiment = "positive"
    elif compound_score <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    # Step 4: Create a dictionary with custom keys
    result = {
        "sentiment": sentiment,
        "compound": compound_score,
        "sentiment_pos": sentiment_scores["pos"],
        "sentiment_neu": sentiment_scores["neu"],
        "sentiment_neg": sentiment_scores["neg"],
    }

    # Step 5: Return the result dictionary
    return result
