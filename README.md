# Fast-API-Text-Summarizer

NLP Processing API

Overview

This is a simple NLP Processing API built using FastAPI. It provides text processing capabilities such as summarization, keyword extraction, and sentiment analysis. The API is powered by transformers, spaCy, TextBlob, and NLTK.

Features

Summarizes input text using facebook/bart-large-cnn.

Extracts keywords using Rake.

Performs sentiment analysis using NLTK's SentimentIntensityAnalyzer.

Stores processed text history.

Requirements

To run this project, ensure you have Python installed and install the required dependencies.

Install Dependencies

pip install fastapi uvicorn transformers spacy textblob rake-nltk nltk

Additionally, download necessary NLTK and spaCy models:

python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('all')"

Running the API

Start the FastAPI application using Uvicorn:
uvicorn main:app --reload

This will start the server at http://127.0.0.1:8000/.

API Endpoints

1. Root Endpoint

URL: /

Method: GET

Description: Returns a welcome message with instructions.

Response:
{"message": "Welcome to the NLP Processing API. Use /docs to explore endpoints."}

2. Process Text

URL: /process

Method: POST

Description: Processes the given text for summarization, keyword extraction, and sentiment analysis.

Request Body:
{
  "text": "Your input text here."
}

Response:
{
  "original_text": "Your input text here.",
  "summary": "Summarized version of the text.",
  "keywords": ["keyword1", "keyword2"],
  "sentiment": "Positive"
}

3. Get History

URL: /history

Method: GET

Description: Retrieves a list of all processed texts.

Response:
[
  {
    "original_text": "Your previous text.",
    "summary": "Summarized text.",
    "keywords": ["keyword1", "keyword2"],
    "sentiment": "Neutral"
  }
]

API Documentation

FastAPI provides an interactive Swagger UI for testing endpoints:

Open http://127.0.0.1:8000/docs in your browser.

Notes

The summarization model (facebook/bart-large-cnn) might take longer to process large texts.

The keyword extraction uses RAKE and may prioritize certain terms over others.

Sentiment analysis is based on NLTK's Vader and works best with English text.

