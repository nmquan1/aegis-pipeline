import google.generativeai as genai # type: ignore
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("API"))
gemini_model = genai.GenerativeModel('gemini-2.0-flash')  

sentiment_task = 'sentiment'
sentiment_model_name = f"cardiffnlp/twitter-roberta-base-{sentiment_task}"

sentiment_tokenizer = AutoTokenizer.from_pretrained(sentiment_model_name)
sentiment_model = AutoModelForSequenceClassification.from_pretrained(sentiment_model_name)