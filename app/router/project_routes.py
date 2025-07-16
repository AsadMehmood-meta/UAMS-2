from flask import render_template
from app import app
from app.model import query

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/projects/list")
def project_list():
    all_projects_query = "SELECT * FROM project ORDER BY created_at"
    projects = query(all_projects_query)
    return render_template("partials/project_list.html", projects=projects)



