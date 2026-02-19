from database.db_connection import get_connection

def insert_threat(threat_type, risk_score, severity, confidence):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO threat_scans (threat_type, risk_score, severity, confidence)
    VALUES (%s, %s, %s, %s)
    RETURNING id;
    """

    cursor.execute(query, (threat_type, risk_score, severity, confidence))
    threat_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return threat_id


def create_case(threat_scan_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO cases (threat_scan_id)
    VALUES (%s);
    """

    cursor.execute(query, (threat_scan_id,))
    conn.commit()
    cursor.close()
    conn.close()


def add_audit_log(action, user_name, result):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO audit_logs (action, user_name, result)
    VALUES (%s, %s, %s);
    """

    cursor.execute(query, (action, user_name, result))
    conn.commit()
    cursor.close()
    conn.close()
