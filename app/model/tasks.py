from app.db import get_db_connection

def get_all_projects():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # get all projects with their IDs (needed to match with tasks)
    cursor.execute("SELECT id, project_title, description FROM project")
    projects = cursor.fetchall()

    # get all tasks
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()

    # Map tasks to their respective project
    for proj in projects:
        proj["tasks"] = [task for task in tasks if task["project_id"] == proj["id"]]

    cursor.close()
    connection.close()
    return projects
