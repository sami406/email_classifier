from flask import Flask, request, jsonify
import model  # Your model loading and prediction code
import masking  # Your PII masking logic

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get input data
    email_text = data.get('email')  # Get email text

    # Mask PII from the email
    masked_email = masking.mask_pii(email_text)

    # Get prediction
    prediction = model.predict(masked_email)

    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

