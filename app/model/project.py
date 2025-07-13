from app.db import get_db_connection

def get_all_projects():
    conection = get_db_connection()
    cursor = conection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM project")
    result = cursor.fetchall()
    
    cursor.close()
    conection.close()
    return result
