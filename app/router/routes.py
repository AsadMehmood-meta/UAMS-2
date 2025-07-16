
from app import app
from flask import render_template, request, redirect, url_for


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

@app.route('/proposals')
def proposals():
    return render_template('proposals.html')

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

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/profile/edit', methods=['GET', 'POST'])
def profile_edit():
    if request.method == 'POST':
        # Here, you’d handle saving the updated data
        # Example: get form data and update the database
        # full_name = request.form['full_name']
        return redirect(url_for('profile'))

    return render_template('profile_edit.html')

if __name__ == '__main__':
    app.run(debug=True)



