
# Email Spam Filter using Python

## Description
This project uses a trained Naive Bayes model with Flask to detect whether an email is spam or not.

## How to Run

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser.

## Model Info
The model is trained on sample spam/ham messages using CountVectorizer and MultinomialNB.
