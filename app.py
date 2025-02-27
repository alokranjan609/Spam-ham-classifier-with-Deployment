from flask import Flask, render_template, request
import joblib
import nltk

# Load the trained model and vectorizer
model = joblib.load("spam_classifier.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Ensure NLTK punkt is downloaded
nltk.download('punkt')

# Preprocessing function (same as before)
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

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email_text = request.form['email_text']  # Get input from form
        transformed_text = transform_text(email_text)  # Preprocess input
        vectorized_text = tfidf.transform([transformed_text]).toarray()  # Convert to TF-IDF
        prediction = model.predict(vectorized_text)[0]  # Predict
        
        result = "Spam" if prediction == 1 else "Not Spam"
        return render_template("index.html", email_text=email_text, prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
