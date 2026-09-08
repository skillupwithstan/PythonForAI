import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize the analyzer
sia = SentimentIntensityAnalyzer()

sample_texts = [
    "I absolutely love how simple Python is for engineering!",
    "This legacy codebase is awful and a complete nightmare to fix."
]

for text in sample_texts:
    scores = sia.polarity_scores(text)
    print(f"Text: '{text}'")
    print(f"Scores: Compound={scores['compound']} | Positive={scores['pos']} | Negative={scores['neg']} | Neutral={scores['neu']}\n")
