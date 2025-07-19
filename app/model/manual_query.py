import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def query(query_string):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    try:
        cursor.execute(query_string)

        # Commit if it's an insert/update/delete
        if query_string.strip().lower().startswith(("insert", "update", "delete", "create", "drop", "alter")):
            connection.commit()

        # Fetch results if it's a SELECT
        if query_string.strip().lower().startswith("select"):
            results = cursor.fetchall()
            return results

    finally:
        cursor.close()
        connection.close()
        
        
def query_one(query_string):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    try:
        cursor.execute(query_string)

        # Commit if it's an insert/update/delete
        if query_string.strip().lower().startswith(("insert", "update", "delete", "create", "drop", "alter")):
            connection.commit()

        # Fetch results if it's a SELECT
        if query_string.strip().lower().startswith("select"):
            results = cursor.fetchone()[0]
            return results

    finally:
        cursor.close()
        connection.close()


