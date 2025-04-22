from flask import Flask, request, jsonify
from model import load_model, predict_category
from masking import mask_pii, unmask_pii

app = Flask(__name__)
model, vectorizer = load_model()


@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    email = data.get("email", "")

    masked_email, pii_data = mask_pii(email)
    category = predict_category(masked_email, model, vectorizer)
    restored_email = unmask_pii(masked_email, pii_data)

    return jsonify({
        "category": category,
        "email": restored_email
    })


if __name__ == "__main__":
    app.run(debug=True)


