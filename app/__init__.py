from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", None)


from  app.router import routes , project_routes , tasks_routes , job_routes
# import app.router