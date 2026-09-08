# pip install transformers torch
# https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion

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

'''
from openai import OpenAI

# Automatically searches for an environment variable named OPENAI_API_KEY
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a precise classifier. Respond with exactly one word choosing from: joy, fear, sadness, anger, neutral."},
        {"role": "user", "content": "I am quite anxious about the system downtime scheduled for tonight."}
    ],
    temperature=0  # Forces highly predictable, deterministic answers
)

print("Detected Emotion:", response.choices[0].message.content.strip())
# Output: fear
'''