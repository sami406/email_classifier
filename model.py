import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
import os

def load_model():
    model = joblib.load("models/classifier.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
    return model, vectorizer

def predict_category(text, model, vectorizer):
    X = vectorizer.transform([text])
    return model.predict(X)[0]
