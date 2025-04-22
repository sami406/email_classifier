from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
import joblib
import os

def train_and_save_model():
    df = pd.read_csv("data/emails.csv")
    X = df["email"]
    y = df["type"]

    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_vectorized, y)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/classifier.pkl")
    joblib.dump(vectorizer, "models/vectorizer.pkl")
    print("✅ Model and vectorizer saved in 'models/' folder")

if __name__ == "__main__":
    train_and_save_model()

