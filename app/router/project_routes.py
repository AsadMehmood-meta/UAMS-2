from flask import render_template
from app import app
from app.model.project import get_all_projects

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/projects/list")
def project_list():
    projects = get_all_projects()
    return render_template("partials/project_list.html", projects=projects)



