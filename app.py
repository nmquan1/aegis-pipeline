import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from utils.process_reviews import process_reviews

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/analyze-review', methods=['POST'])
def analyze_review():
    data = request.json
    
    reviews = data.get('reviews', [])
    if not reviews:
        return jsonify({"error": "No reviews provided"}), 400

    result = process_reviews(reviews)

    return jsonify({
        "comments": result['reviews'],
        "average_lgbt_friendliness": result['average_lgbt_friendliness'],
        "average_black_friendliness": result['average_black_friendliness'],
        "summary": result['summary'],
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)