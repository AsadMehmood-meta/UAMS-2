from flask import render_template , request , redirect , url_for
from app import app
from app.model import query

@app.route("/assigned_tasks")
def assigned_tasks():
    return render_template("assigned_tasks.html")


@app.route("/assigned_tasks/list")
def assigned_tasks_table():
    assigned_tasks_query = "SELECT t.task_title AS tasks_title, p.project_title AS project_title, CONCAT(u.first_name, ' ', u.last_name) AS assigned_to, a.assigned_date, t.deadline, t.status FROM assignment a JOIN task t ON a.task_id = t.task_id JOIN project p ON t.project_id = p.project_id JOIN user u ON a.user_id = u.user_id;"
    assigned_tasks = query(assigned_tasks_query)
    return render_template("partials/assigned_tasks_table.html", assigned_tasks_table=assigned_tasks)

@app.route("/assigned_tasks/list/<int:project_id>")
def project_tasks(project_id):
    project_tasks_query = f"SELECT * FROM task WHERE project_id = {project_id}"
    assigned_tasks = query(project_tasks_query)
    return render_template("partials/project_tasks.html", project_tasks=assigned_tasks)


@app.route("/task/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    delete_query = f"DELETE FROM task WHERE task_id = {task_id}"
    query(delete_query)
    return "No content available to delete", 204 


@app.route("/tasks/submit", methods=["POST"])
def submit_new_task():
    title = request.form["task_title"]
    description = request.form["description"]
    priority = request.form["priority"]
    deadline = request.form["deadline"]
    project_id = request.form["project_id"]
    comment = request.form.get("comment", "")
    user_id = request.form["user_id"]

    insert_task_query = f"""
    INSERT INTO task (
        task_title, description, comment, priority, deadline, project_id, user_id
    )
    VALUES (
        '{title}', '{description}', '{comment}', '{priority}', '{deadline}', {project_id}, {user_id}
    )
    """
    query(insert_task_query)

    return redirect(url_for("project_task", project_id=project_id))



 
@app.route("/tasks/add/<int:project_id>")
def add_task_form(project_id):
    # Fetch members only
    users_query = "SELECT user_id, CONCAT(first_name, ' ', last_name) AS full_name FROM user WHERE role = 'Member'"
    users = query(users_query)
    return render_template("partials/add_task_form.html", project_id=project_id, users=users)

