# Sentiment Analysis Tool

A Python-based tool that classifies text sentiment using LSTM and logistic regression models. The tool includes preprocessing steps, model training, and evaluation, achieving around 89% accuracy.

## Tech Stack

- Python  
- TensorFlow  
- NLTK  
- Scikit-learn  

## Usage

1. Clone the repository:

bash
git clone https://github.com/mahiyafatima/sentiment-analysis-tool.git
cd sentiment-analysis-tool
Run the sentiment analysis script:

bash

python sentiment_analysis.py
Provide input text to classify sentiment.

Features
Text preprocessing with NLTK

Sentiment classification using LSTM and logistic regression

Model evaluation and accuracy measurement

Project Structure

sentiment-analysis-tool/
├── main.py                  # Main script for sentiment analysis
├── sentiment_analysis.py    # Sentiment analysis module/script
├── mytext.txt               # Sample input text file
├── README.md                # Project documentation
Requirements
Install dependencies with:


pip install tensorflow nltk scikit-learn
For first-time NLTK usage, download necessary data:

python

import nltk
nltk.download('punkt')
nltk.download('stopwords')
Author
Mahiya Fatima
Email: mahiyafatima071@gmail.com

License
This project is for educational purposes and open for personal or academic use.

yaml
Copy code
