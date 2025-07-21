import spacy
from textblob import TextBlob

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to analyze sentiment using TextBlob
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Positive or negative sentiment
    subjectivity = blob.sentiment.subjectivity  # How subjective the text is
    return polarity, subjectivity

# Example text
text = "I love working with spaCy and TextBlob!"

# Process text with spaCy
doc = nlp(text)

# Get sentiment values using TextBlob
polarity, subjectivity = get_sentiment(text)

# Output the sentiment results
print(f"Text: {text}")
print(f"Polarity: {polarity}")
print(f"Subjectivity: {subjectivity}")

