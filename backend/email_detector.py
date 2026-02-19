from database.queries import insert_threat, create_case, add_audit_log

def analyze_email(text):

    # Example logic
    risk_score = 0.92
    confidence = 92.0

    if risk_score > 0.8:
        severity = "High"
    elif risk_score > 0.5:
        severity = "Medium"
    else:
        severity = "Low"

    # Save to database
    threat_id = insert_threat(
        "Email Phishing",
        risk_score,
        severity,
        confidence
    )

    if risk_score > 0.8:
        create_case(threat_id)

    add_audit_log(
        action="Email Scan",
        user_name="Vaibhavi",
        result=severity
    )

    return {
        "risk_score": risk_score,
        "severity": severity,
        "confidence": confidence,
        "explanation": "Detected AI-generated phishing patterns."
    }

