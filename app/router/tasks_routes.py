from flask import render_template
from app import app
from app.model.tasks import get_assigned_tasks

@app.route("/assigned_tasks")
def assigned_tasks():
    return render_template("assigned_tasks.html")

@app.route("/assigned_tasks/list")
def assigned_tasks_table():
    assigned_tasks = get_assigned_tasks()
    return render_template("partials/assigned_tasks_table.html", assigned_tasks_table=assigned_tasks)
