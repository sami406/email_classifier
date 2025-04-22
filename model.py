# model.py
import joblib

def load_model_and_vectorizer():
    model = joblib.load("models/classifier.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
    return model, vectorizer

def predict_category(text, model, vectorizer):
    X = vectorizer.transform([text])
    return model.predict(X)[0]
