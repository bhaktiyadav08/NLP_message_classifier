# data/sample_data.py

# Priority classification
priority_texts = [
    "urgent meeting",
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
    "thank you"
]
complaint_labels = ["Abusive", "Abusive", "Normal", "Normal"]

# Message type classification
type_texts = [
    "meeting at 5 pm",
    "deadline submission",
    "let's hangout",
    "project meeting"
]
type_labels = ["Meeting", "Deadline", "Casual", "Meeting"]
