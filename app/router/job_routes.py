from flask import render_template
from app import app
from app.model import query

@app.route("/jobs")
def jobs():
    return render_template("jobs.html")



@app.route("/jobs/list")
def all_jobs():
    all_jobs_query = "SELECT * FROM job"
    all_jobs = query(all_jobs_query)
    return render_template("partials/all_jobs.html", all_jobs=all_jobs)



