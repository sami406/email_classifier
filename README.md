# Email Classification System with PII Masking

This project classifies incoming support emails into predefined categories (e.g., Billing Issues, Technical Support, Account Management) while ensuring that personal information (PII) is masked before processing. The PII is restored after classification.

## Table of Contents
- [Introduction](#introduction)
- [Setup Instructions](#setup-instructions)
- [API Usage](#api-usage)
- [Model Details](#model-details)
- [Deployment](#deployment)

## Introduction
The goal of this project is to design and implement an email classification system for a company's support team. The system categorizes incoming support emails and masks personal information (PII) for privacy.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/email_classifier.git
   cd email_classifier




2. Set up a virtual environment (optional but recommended):
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies:
bash
Copy code
pip install -r requirements.txt


4.To train the model, run:
bash
Copy code
python train_model.py

5.To start the Flask app locally:
bash
Copy code
python app.py


6.The API will be available at http://127.0.0.1:5000.

   



## API Usage
Endpoint: /classify
Method: POST

Request: Send an email in the body as JSON:

json
Copy code
{
  "email": "Hello, my name is John Doe and my email is johndoe@example.com. I have a billing issue."
}
Response: Classify the email and restore masked PII:

json
Copy code
{
  "category": "Billing Issues",
  "email": "Hello, my name is [full_name] and my email is [email]. I have a billing issue."
}


## Model Details
Model used: Random Forest Classifier (You can replace it with other models as needed)

Training script: train_model.py

Model file: models/classifier.pkl

## Deployment

The primary goal of this project is to create a robust email classification system for customer support teams. The system not only classifies emails into predefined categories such as "Billing Issues," "Technical Support," or "Account Management" but also ensures that any personally identifiable information (PII) is masked to maintain user privacy. The masked PII is later restored after the classification is complete.

---

#### **Approach Taken for PII Masking and Classification**

This section should describe how you handled the PII masking and classification. Mention the methods used for both.

Example:

> PII masking is performed using a combination of **Named Entity Recognition (NER)** and **regular expressions** (Regex). The key fields such as names, email addresses, phone numbers, and credit card details are detected and replaced with placeholders like `[full_name]`, `[email]`, `[phone_number]`, etc.  
> For classification, we used a **Logistic Regression** classifier to categorize emails based on their content. The model was trained using the dataset containing labeled emails.

---

#### **Model Selection and Training Details**

Provide a brief explanation of the model selection and training process.

Example:

> The **Logistic Regression** model was selected for this classification task due to its ability to handle high-dimensional data and provide robust performance. The model was trained using a preprocessed dataset containing labeled email data. The `train_model.py` script was used to train the model and save the trained model to `classifier.pkl`. We used **TF-IDF vectorization** to convert the email text into numerical features suitable for the Random Forest model.

---

#### **Challenges Faced and Solutions Implemented**

Discuss any challenges you encountered and how you addressed them.

Example:

> One challenge encountered during the development process was handling **PII masking** in a way that doesn't interfere with the email classification process. Initially, it was difficult to detect certain types of PII (e.g., phone numbers or credit card details) accurately, but by using a combination of **NER** and **Regex**, we were able to handle this effectively.  
> Another challenge was ensuring the model’s **accuracy** while keeping the system **lightweight** for real-time deployment. We used **Random Forest** due to its balance between accuracy and computational efficiency.

---

### **4. Final Output: API Endpoint Details for Testing**

Finally, make sure to mention the **API endpoint** and how users can interact with it for testing:

- **API Endpoint**: `POST /classify`
- **Input**: JSON containing the email text.
- **Output**: The classified category and the email with masked PII.

---

### **Summary:**

- **Code Implementation**: Completed with all scripts, model training, and API setup.
- **API Details**: Provided in the `README.md` for testing.
- **Report**: Includes an overview of the problem, approach, challenges, and model details.


