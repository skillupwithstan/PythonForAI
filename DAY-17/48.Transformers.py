from transformers import pipeline

# Load the verified emotion text-classification pipeline 
classifier = pipeline(
    "text-classification", 
    model="bhadresh-savani/distilbert-base-uncased-emotion"
)

results = classifier([
    "I just finished building my first ML model and it works perfectly!",
    "I am quite anxious about the system downtime scheduled for tonight."
])

# Print the text along with its corresponding prediction
sentences = [
    "I just finished building my first ML model and it works perfectly!",
    "I am quite anxious about the system downtime scheduled for tonight."
]

for sentence, res in zip(sentences, results):
    print(f"\nText: '{sentence}'")
    print(f"Detected Emotion: {res['label']} (Confidence Score: {round(res['score'], 4)})")
