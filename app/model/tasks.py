from app.db import get_db_connection

assigned_tasks_query = "SELECT t.task_title AS tasks_title, p.project_title AS project_title, CONCAT(u.first_name, ' ', u.last_name) AS assigned_to, a.assigned_date, t.deadline, t.status FROM assignment a JOIN task t ON a.task_id = t.task_id JOIN project p ON t.project_id = p.project_id JOIN user u ON a.user_id = u.user_id;"


def get_all_tasks():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # get assigned tasks tasks
    cursor.execute("SELECT * FROM task")
    all_tasks = cursor.fetchall()

    cursor.close()
    connection.close()
    return all_tasks


def get_assigned_tasks():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # get assigned tasks tasks
    cursor.execute(assigned_tasks_query)
    assigned_tasks = cursor.fetchall()

    cursor.close()
    connection.close()
    return assigned_tasks
