from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

messages = [
    "urgent meeting",
    "project deadline tomorrow",
    "please respond",
    "important update",
    "hello bro",
    "let's hangout",
    "good morning",
    "what's up"
]

labels = [1, 1, 1, 1, 0, 0, 0, 0]
stop_words=set(stopwords.words('english'))
def remove_stopwords(messages):
  return " ".join([word for word in messages.split() if word.lower() not in stop_words])
cleaned_sentences=[remove_stopwords(s) for s in messages]
print("After stopword removal:")
print(cleaned_sentences)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(cleaned_sentences)

print(vectorizer.get_feature_names_out())
print(X.toarray())

nb_model = MultinomialNB()
nb_model.fit(X, labels)

test_messages = ["urgent meeting"]
test_vectors = vectorizer.transform(test_messages)
nb_pred = nb_model.predict(test_vectors)
for prediction in nb_pred:
 if prediction == 1:
  print("High")
 else:
  print("low")