# models/train_model.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from data.sample_data import (
    priority_texts, priority_labels,
    complaint_texts, complaint_labels,
    type_texts, type_labels
)
from utils.preprocess import clean_text

# 🔹 Preprocess data
priority_clean = [clean_text(s) for s in priority_texts]
complaint_clean = [clean_text(s) for s in complaint_texts]
type_clean = [clean_text(s) for s in type_texts]

# 🔹 Vectorizers
p_vec = CountVectorizer()
c_vec = CountVectorizer()
t_vec = CountVectorizer()

X_p = p_vec.fit_transform(priority_clean)
X_c = c_vec.fit_transform(complaint_clean)
X_t = t_vec.fit_transform(type_clean)

# 🔹 Models
p_model = MultinomialNB().fit(X_p, priority_labels)
c_model = MultinomialNB().fit(X_c, complaint_labels)
t_model = MultinomialNB().fit(X_t, type_labels)


# 🔥 Prediction Function
def predict_message(message):
    cleaned = clean_text(message)

    p_input = p_vec.transform([cleaned])
    c_input = c_vec.transform([cleaned])
    t_input = t_vec.transform([cleaned])

    return {
        "message": message,
        "priority": str(p_model.predict(p_input)[0]),
        "complaint": str(c_model.predict(c_input)[0]),
        "type": str(t_model.predict(t_input)[0])
    }