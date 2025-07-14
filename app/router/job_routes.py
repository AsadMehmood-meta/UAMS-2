from flask import render_template
from app import app
from app.model.jobs import get_all_jobs

@app.route("/jobs")
def jobs():
    return render_template("jobs.html")

@app.route("/jobs/list")
def all_jobs():
    all_jobs = get_all_jobs()
    return render_template("partials/all_jobs.html", all_jobs=all_jobs)



