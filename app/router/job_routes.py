from flask import render_template
from app import app
from app.model.manual_query import query , query_one
from app.utilities.job_scraper import scrape_jobs 
import logging


@app.route("/jobs")
def jobs():
    return render_template("jobs.html")



@app.route("/jobs/list")
def all_jobs():
    all_jobs_query = "SELECT * FROM job ORDER BY job_id DESC"
    all_jobs = query(all_jobs_query)
    return render_template("partials/all_jobs.html", all_jobs=all_jobs)

def is_job_exists(job_link):
    is_job_exists_query = "SELECT COUNT(*) FROM job WHERE url_link = %s", (job_link,)
    count = query_one(is_job_exists_query)
    return count > 0

def save_jobs_to_db(jobs):
    for job in jobs:
        title = job.get("title", "").replace("'", "''")
        url_link = job.get("url_link", "").replace("'", "''")

        insert_query = f"""
        INSERT INTO job (title, url_link)
        VALUES ('{title}', '{url_link}')
        """
        query(insert_query)


@app.route("/scrape-jobs", methods=["POST"])
def scrape_and_save_jobs():
    try:
        scraped_jobs = scrape_jobs()  
        saved_count = 0

        for job_data in scraped_jobs:
            job_link = job_data.get("url_link", "")

            if not is_job_exists(job_link):
                save_jobs_to_db(job_data)
                saved_count += 1
            else:
                logging.info(f"Job already exists: {job_link}")

        logging.info(f"{saved_count} new jobs saved to database.")

    except Exception as e:
        logging.error(f"Error in scraping or saving jobs: {str(e)}")

    return render_template("jobs.html")

# @app.route("/scrape-jobs", methods=["POST"])
# def scrape_and_reload():
#     try:
#         scrape_jobs_() 
#         print("hello")
#     except Exception as e:
#         print(f"Error while scraping: {e}")
    
#     return render_template("jobs.html")