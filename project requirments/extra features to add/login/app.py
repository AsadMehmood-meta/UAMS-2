from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change to a secure random key

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'uamsdb'

mysql = MySQL(app)

# Helper function to validate email
def is_valid_email(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_pattern, email)

# Helper function to validate phone
def is_valid_phone(phone):
    phone_pattern = r'^\d{10,12}$'
    return re.match(phone_pattern, phone)

@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('home.html', username=session['username'], role=session['role'])
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']  # Store password in plain text
        phone = request.form['phone']
        email = request.form['email']
        role = request.form.get('role', 'member')  # Default to 'member'

        # Input validation
        if not all([first_name, last_name, username, password, phone, email]):
            flash('All fields are required!', 'error')
            return render_template('signup.html')

        if not is_valid_email(email):
            flash('Invalid email format!', 'error')
            return render_template('signup.html')

        if not is_valid_phone(phone):
            flash('Invalid phone number! Must be 10-12 digits.', 'error')
            return render_template('signup.html')

        # Check if username or email already exists
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user WHERE username = %s OR email = %s", (username, email))
        existing_user = cur.fetchone()
        if existing_user:
            flash('Username or email already exists!', 'error')
            cur.close()
            return render_template('signup.html')

        # Insert user with plain text password
        cur.execute(
            "INSERT INTO user (first_name, last_name, username, password, phone, email, role) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (first_name, last_name, username, password, phone, email, role)
        )
        mysql.connection.commit()
        cur.close()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM user WHERE username = %s", (username,))
            user = cur.fetchone()
            cur.close()

            if user and user[7] == password:  # user[4] is password, compare plain text
                session['user_id'] = user[0]  # user[0] is id
                session['username'] = user[3]  # user[3] is username
                session['role'] = user[6]      # user[6] is role
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password!', 'error')
        except Exception as e:
            flash(f'Database error: {str(e)}', 'error')
            print(e)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first!', 'error')
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'], role=session['role'])

if __name__ == '__main__':
    app.run(debug=True)