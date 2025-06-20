
from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        input_text = request.form["email_text"]
        vector_input = vectorizer.transform([input_text])
        result = model.predict(vector_input)[0]
        prediction = "Spam" if result == 1 else "Not Spam"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
