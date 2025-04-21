import re

PII_PATTERNS = {
    "full_name": r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b",
    "email": r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
    "phone_number": r"\b(?:\+91[-\s]?|0)?[6-9]\d{9}\b",
    "dob": r"\b(?:\d{2}[/-]){2}\d{4}\b",
    "aadhar_num": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/?([0-9]{2}|[0-9]{4})\b"
}

def mask_pii(text):
    original = {}
    for key, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            for match in matches:
                real_match = match if isinstance(match, str) else match[0]
                original[f"[{key}]"] = real_match
                text = text.replace(real_match, f"[{key}]")
    return text, original

def unmask_pii(masked_text, original):
    for key, value in original.items():
        masked_text = masked_text.replace(key, value)
    return masked_text
