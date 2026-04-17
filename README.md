# 📩 NLP Message Classification System

A simple **Natural Language Processing (NLP)** project that classifies messages into multiple categories using Machine Learning.

---

## 🚀 Features

* 🔴 **Priority Classification**
  Classifies messages as:
  → High / Medium / Low

* ⚠️ **Complaint Detection**
  Detects whether a message is:
  → Abusive / Normal

* 💬 **Message Type Classification**
  Identifies message intent:
  → Meeting / Deadline / Casual

---

## 🧠 Tech Stack

* Python
* Scikit-learn
* CountVectorizer (Bag of Words)
* Multinomial Naive Bayes
* Logistic Regression (for comparison)

---

## ⚙️ How It Works

1. **Text Preprocessing**

   * Tokenization
   * Stopwords Removal

2. **Vectorization**

   * Convert text → numerical form using CountVectorizer

3. **Model Training**

   * Train classifiers on dummy dataset

4. **Prediction**

   * Input message → Model predicts:

     * Priority
     * Complaint type
     * Message category

---

## 📊 Example

**Input:**

```text
urgent meeting at 5 pm
```

**Output:**

```text
Priority  : High
Complaint : Normal
Type      : Meeting
```

---

## 🛠️ Installation & Usage

```bash
# Clone repository
git clone https://github.com/your-username/your-repo-name.git

# Navigate to folder
cd your-repo-name

# Install dependencies
pip install -r requirements.txt

# Run notebook or script
```

---

## 📁 Project Structure

```text
├── notebook.ipynb        # Model training & testing
├── model files (optional)
├── README.md
```

---

## 🎯 Learning Outcomes

* Understood NLP preprocessing techniques
* Learned text vectorization using CountVectorizer
* Implemented Naive Bayes & Logistic Regression
* Built a multi-task text classification system

---

## 🚀 Future Improvements

* Use real-world datasets
* Apply TF-IDF vectorization
* Improve accuracy with more training data
* Build Flask API for deployment
* Add frontend UI


