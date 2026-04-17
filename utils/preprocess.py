# utils/preprocess.py

import nltk
from nltk.corpus import stopwords

# download once
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(sentence):
    return " ".join([
        word for word in sentence.split()
        if word.lower() not in stop_words
    ])