import re

def mask_pii(text):
    pii_data = {}

    patterns = {
        "full_name": r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b",
        "email": r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
        "phone_number": r"\b[789]\d{9}\b",
        "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
        "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",
        "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
        "cvv_no": r"\b\d{3}\b",
        "expiry_no": r"\b(0[1-9]|1[0-2])\/?([0-9]{2})\b"
    }

    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            pii_data[key] = matches
            text = re.sub(pattern, f"[{key}]", text)

    return text, pii_data

def unmask_pii(text, pii_data):
    for key, values in pii_data.items():
        for value in values:
            text = text.replace(f"[{key}]", value, 1)
    return text

