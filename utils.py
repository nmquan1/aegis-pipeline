import re
import numpy as np
from scipy.special import softmax
from deep_translator import GoogleTranslator
from nltk.corpus import stopwords
import csv
import urllib.request
from model_loader import sentiment_tokenizer, sentiment_model, gemini_model

# Load sentiment labels
mapping_link = "https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/sentiment/mapping.txt"
with urllib.request.urlopen(mapping_link) as f:
    labels = [row[1] for row in csv.reader(f.read().decode('utf-8').split("\n"), delimiter='\t') if len(row) > 1]

translator = GoogleTranslator()

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)
    text = text.lower()
    text = " ".join([word for word in text.split() if word not in stopwords.words('english')])
    return text


def get_friendliness_score(text, community):
    prompt = f"""
    Rate the offensiveness towards {community} strictly from 0.10 to 0.39.
    of the following comment:   
    Comment: "{text}"
    If it's negative but irrelevant to this community, return 0.4
    """
    try:
        response = gemini_model.generate_content(prompt)
        matches = re.findall(r"[0-9]*\.?[0-9]+", response.text.strip())

        if matches:
            score = float(matches[0])
            return score
    except Exception as e:
        print(f"Friendliness score failed: {e}")
    return 0.5  # Return a default score if the model fails



def generate_summary(comments):
    joined = "\n".join(comments)
    prompt = f"""Summarize the following comments:\n{joined} Only include the most relevant information. 
    Provide just the summary, nothing else."""

    try:
        response = gemini_model.generate_content(prompt)

        if hasattr(response, 'text') and response.text.strip():
            return response.text.strip()
    except Exception as e:
        print(f"Summary generation failed: {e}")

    return "No summary available."


def process_reviews(reviews):
    results = []
    texts = []

    for review in reviews:
        text = review['comment']
        texts.append(text)

        #clean = clean_text(text)
        #trans = translator.translate(clean, target='en')

        # Sentiment analysis
        tokens = sentiment_tokenizer(text, return_tensors="pt")
        output = sentiment_model(**tokens)
        scores = softmax(output[0][0].detach().numpy())
        sentiment = labels[np.argmax(scores)]


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



