
from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from masking import mask_pii  # assuming you have this utility for PII masking

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("models/classifier.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    # Get the JSON data sent from the client
    data = request.json
    text = data.get("text", "")

    # Preprocess and predict
    if text:
        X = vectorizer.transform([text])
        prediction = model.predict(X)
        result = {
            "prediction": prediction[0],
            "text": mask_pii(text)  # Mask any PII from the text
        }
        return jsonify(result)
    return jsonify({"error": "No text provided"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)

