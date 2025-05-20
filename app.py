from flask import Flask, render_template, request
import joblib
import nltk
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load("spam_classifier.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Ensure required NLTK data is available
nltk.data.path.append(os.path.join(os.getcwd(), 'nltk_data'))
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=os.path.join(os.getcwd(), 'nltk_data'))

# Preprocessing function
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email_text = request.form['email_text']
        transformed_text = transform_text(email_text)
        vectorized_text = tfidf.transform([transformed_text]).toarray()
        prediction = model.predict(vectorized_text)[0]

        result = "Spam" if prediction == 1 else "Not Spam"
        return render_template("index.html", email_text=email_text, prediction=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
