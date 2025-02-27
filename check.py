import joblib

# Load the trained TF-IDF vectorizer
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Ensure it is fitted
if not hasattr(tfidf, "idf_"):  # "idf_" attribute exists only in fitted vectorizers
    raise ValueError("Loaded TF-IDF vectorizer is not fitted!")

# Use the loaded vectorizer for transformation
email_text = "Your email content here..."
vectorized_text = tfidf.transform([email_text]).toarray()

print("Vectorization successful:", vectorized_text)