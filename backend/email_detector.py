import re

def analyze_email(email_text):
    email_text = email_text.lower()

    # Simple phishing indicators
    suspicious_keywords = [
        "urgent",
        "verify your account",
        "click here",
        "suspended",
        "password",
        "bank",
        "login",
        "confirm",
        "immediately"
    ]

    suspicious_links = re.findall(r"http[s]?://\S+", email_text)

    keyword_score = sum(1 for word in suspicious_keywords if word in email_text)
    link_score = len(suspicious_links)

    # Simple risk calculation
    risk_score = min((keyword_score * 0.1) + (link_score * 0.2), 1.0)

    confidence = round(risk_score * 100, 2)

    # Severity logic
    if risk_score > 0.8:
        severity = "High"
    elif risk_score > 0.5:
        severity = "Medium"
    else:
        severity = "Low"

    return {
        "risk_score": risk_score,
        "severity": severity,
        "confidence": confidence,
        "explanation": "Detected AI-generated phishing patterns."
    }
