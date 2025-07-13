from app import app
from flask import render_template , request

@app.route('/')
def home():
    return render_template('home.html') # default home

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html') , 200

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # signup logic here (e.g., save to DB)
        return "Signup form submitted"
    return render_template('signup.html')

@app.route('/budget')
def budget():
    return render_template('budget.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route("/all_jobs")
def all_jobs():
    jobs = [
        {
            "title": "Build a Flask Web App",
            "description": "Looking for someone to build a Flask app to manage my freelancing workflow...",
            "category": "Web Dev",
            "budget": 150
        },
        {
            "title": "Create Upwork Proposal Templates",
            "description": "Need a proposal generator for Upwork job scraping system with dynamic fields...",
            "category": "Content Writing",
            "budget": 80
        },
        {
            "title": "Automate Upwork Bidding",
            "description": "Want to scrape jobs from Upwork and auto-send proposals using Python + Selenium.",
            "category": "Automation",
            "budget": 200
        }
    ]
    return render_template("all_jobs.html", jobs=jobs) # All Jobs

@app.route('/feasibility')
def feasibility():
    return render_template('feasibility.html')

@app.route('/proposals')
def proposals():
    return render_template('proposals.html')

@app.route("/assigned_tasks")
def assigned_tasks():
    return render_template("assigned_tasks.html")  # Assigned Tasks

@app.route('/team_taskboard')
def team_taskboard():
    return render_template('team_taskboard.html')

@app.route("/project_deadlines")
def project_deadlines():
    return render_template("project_deadlines.html")


@app.route('/team_overview')
def team_overview():
    return render_template('team_overview.html')

@app.route('/roles_permissions')
def roles_permissions():
    return render_template('roles_permissions.html')

@app.route("/operational_reports")
def operational_reports():
    return render_template("operational_reports.html")

@app.route('/proposal_success')
def proposal_success():
    return render_template('proposal_success.html')

@app.route('/productivity')
def productivity():
    return render_template('productivity.html')

@app.route('/logout')
def logout():
    return "You have been logged out (placeholder)"

if __name__ == '__main__':
    app.run(debug=True)
