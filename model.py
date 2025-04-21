# model.py

import pickle

def predict_category(text):
    with open("models/classifier.pkl", "rb") as f:
        tfidf, model = pickle.load(f)
    X = tfidf.transform([text])
    return model.predict(X)[0]
