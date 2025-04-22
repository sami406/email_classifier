import gradio as gr
from masking import mask_pii
from model import load_model_and_vectorizer, predict_category

# Load model and vectorizer once
model, vectorizer = load_model_and_vectorizer()

def classify_email(email_text):
    masked_email = mask_pii(email_text)
    category = predict_category(masked_email, model, vectorizer)
    return category, masked_email

# Gradio Interface
iface = gr.Interface(
    fn=classify_email,
    inputs=gr.Textbox(lines=10, label="Enter Support Email"),
    outputs=[
        gr.Textbox(label="Predicted Category"),
        gr.Textbox(label="Masked Email")
    ],
    title="Email Classification System with PII Masking",
    description="Enter a customer support email to classify it into a predefined category after masking personal information."
)

if __name__ == "__main__":
    iface.launch()
