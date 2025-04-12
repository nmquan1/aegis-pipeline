import google.generativeai as genai
from transformers import AutoTokenizer, AutoModelForSequenceClassification


genai.configure(api_key="AIzaSyBE-vm3wSuOp-h0ylqE0MUKoGAuP_K1dDQ")
gemini_model = genai.GenerativeModel('gemini-2.0-flash')  


sentiment_task = 'sentiment'
sentiment_model_name = f"cardiffnlp/twitter-roberta-base-{sentiment_task}"

sentiment_tokenizer = AutoTokenizer.from_pretrained(sentiment_model_name)
sentiment_model = AutoModelForSequenceClassification.from_pretrained(sentiment_model_name)
