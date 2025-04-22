
from flask import Flask, request, jsonify
from masking import mask_pii
from model import load_model_and_vectorizer, predict_category

app = Flask(__name__)
model, vectorizer = load_model_and_vectorizer()

@app.route("/classify", methods=["POST"])
def classify_email():
    data = request.json
    email = data.get("email", "")
    masked_email, _ = mask_pii(email)
    category = predict_category(model, vectorizer, masked_email)
    return jsonify({"email": email, "category": category})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
