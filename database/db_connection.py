import psycopg2

def get_connection():
    return psycopg2.connect(
        database="secureai_db",
        user="postgres",
        password="0822",
        host="localhost",
        port="5432"
    )
