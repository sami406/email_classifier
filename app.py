from flask import Flask, request, jsonify
from masking import mask_pii, unmask_pii
from model import predict_category

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify_email():
    data = request.json
    email_text = data.get("email", "")

    # Mask PII
    masked_text, original_data = mask_pii(email_text)

    # Predict category
    category = predict_category(masked_text)

    # Unmask text
    restored_text = unmask_pii(masked_text, original_data)

    return jsonify({
        "category": category,
        "email": restored_text
    })

if __name__ == "__main__":
    app.run(debug=True)
