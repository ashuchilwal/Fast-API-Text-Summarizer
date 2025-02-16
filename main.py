from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import spacy
from textblob import TextBlob
from typing import List
from rake_nltk import Rake
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk


# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('vader_lexicon')
nltk.download('all')


app = FastAPI()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
nlp = spacy.load("en_core_web_sm")


nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


history = []

class TextRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to the NLP Processing API. Use /docs to explore endpoints."}

@app.post("/process")
def process_text(request: TextRequest):
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text field cannot be empty.")
    
    
    if len(text.split()) < 30:  
        summary = text
    else:
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    
     
    rake = Rake()
    rake.extract_keywords_from_text(text)
    keywords = rake.get_ranked_phrases()
    

    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        sentiment_label = "Positive"
    elif sentiment_score['compound'] <= -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    result = {
        "original_text": text,
        "summary": summary,
        "keywords": keywords,
        "sentiment": sentiment_label
    }
    
    history.append(result)
    return result

@app.get("/history")
def get_history():
    if not history:
        raise HTTPException(status_code=404, detail="No processed texts available.")
    return history

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)