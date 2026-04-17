from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

# Priority classification
priority_texts = [
    "urgent meeting now",
    "project deadline tomorrow",
    "please check this",
    "hello bro",
    "good morning"
]

priority_labels = ["High", "High", "Medium", "Low", "Low"]
# Complaint detection
complaint_texts = [
    "this service is terrible",
    "you are useless",
    "I need help",
    "thank you so much"
]

complaint_labels = ["Abusive", "Abusive", "Normal", "Normal"]
# Message type classification
type_texts = [
    "meeting at 5 pm",
    "deadline submission today",
    "let's hangout",
    "project discussion meeting"
]

type_labels = ["Meeting", "Deadline", "Casual", "Meeting"]

# Priority model
priority_vectorizer = CountVectorizer()
X_priority = priority_vectorizer.fit_transform(priority_texts)

priority_model = MultinomialNB()
priority_model.fit(X_priority, priority_labels)

# Complaint model
complaint_vectorizer = CountVectorizer()
X_complaint = complaint_vectorizer.fit_transform(complaint_texts)

complaint_model = MultinomialNB()
complaint_model.fit(X_complaint, complaint_labels)


# Type model
type_vectorizer = CountVectorizer()
X_type = type_vectorizer.fit_transform(type_texts)

type_model = MultinomialNB()
type_model.fit(X_type, type_labels)
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    return "API is running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    message = data['message']

    # Transform input
    p_vec = priority_vectorizer.transform([message])
    c_vec = complaint_vectorizer.transform([message])
    t_vec = type_vectorizer.transform([message])

    # Predictions
    priority = priority_model.predict(p_vec)[0]
    complaint = complaint_model.predict(c_vec)[0]
    msg_type = type_model.predict(t_vec)[0]

    return jsonify({
        "message": message,
        "priority": priority,
        "complaint": complaint,
        "type": msg_type
    })

if __name__ == '__main__':
    app.run(debug=True)