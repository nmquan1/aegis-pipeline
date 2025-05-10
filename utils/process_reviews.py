import csv
import numpy as np
from scipy.special import softmax
import urllib
from utils.prompt import generate_summary, get_friendliness_score
from config.config import sentiment_model, sentiment_tokenizer

# Load labels here (instead of importing directly)
mapping_link = "https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/sentiment/mapping.txt"
with urllib.request.urlopen(mapping_link) as f:
    labels = [row[1] for row in csv.reader(f.read().decode('utf-8').split("\n"), delimiter='\t') if len(row) > 1]

def process_reviews(reviews):
    results = []
    texts = []

    for review in reviews:
        text = review['comment']
        texts.append(text)

        # Sentiment analysis
        tokens = sentiment_tokenizer(text, return_tensors="pt")
        output = sentiment_model(**tokens)
        scores = softmax(output[0][0].detach().numpy())
        sentiment = labels[np.argmax(scores)]  # Using labels loaded above

        # Friendliness scoring
        if sentiment.lower() == "negative":
            lgbt_friendliness = get_friendliness_score(text, 'LGBTQ+ Friendly')
            black_friendliness = get_friendliness_score(text, 'Black Friendly')
        else:
            lgbt_friendliness = 0.4 
            black_friendliness = 0.4

        results.append({
            "original": text,
            "sentiment": sentiment, 
            "lgbt_friendliness_score": lgbt_friendliness,
            "black_friendliness_score": black_friendliness
        })

    avg_lgbt_friendliness = np.mean([r['lgbt_friendliness_score'] for r in results])
    avg_black_friendliness = np.mean([r['black_friendliness_score'] for r in results])

    summary = generate_summary(texts)

    return {
        "reviews": results,  
        "average_lgbt_friendliness": round(avg_lgbt_friendliness, 4),
        "average_black_friendliness": round(avg_black_friendliness, 4),
        "summary": summary,
    }
