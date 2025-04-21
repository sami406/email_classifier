# train_model.py

import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

def train_and_save_model():
    # Load data
    df = pd.read_csv("data/emails.csv")  # Make sure this file exists

    # Feature extraction
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(df["email"])
    y = df["type"]

    # Train model
    model = LogisticRegression()
    model.fit(X, y)

    # Save model and vectorizer together
    os.makedirs("models", exist_ok=True)
    with open("models/classifier.pkl", "wb") as f:
        pickle.dump((tfidf, model), f)

    print("✅ Model saved to models/classifier.pkl")

if __name__ == "__main__":
    train_and_save_model()
