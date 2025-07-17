from textblob import TextBlob
'''from newspaper import Article'''

# Analysis Of Article 
'''url = 'https://us.cnn.com/2025/04/03/investing/us-stock-market/index.html'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print (sentiment)'''

# Analtsis Of Own Text

with open(r'C:\Users\Mugeesh\Desktop\Projects\Simple Sentiment Text Analysis\mytext.txt', 'r') as f:
    text = f.read()


blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print (sentiment)
