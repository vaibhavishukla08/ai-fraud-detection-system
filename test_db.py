from database.queries import insert_threat

threat_id = insert_threat("Test Threat", 0.75, "Medium", 88)

print("Inserted Threat ID:", threat_id)
