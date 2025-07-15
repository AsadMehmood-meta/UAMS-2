
from app import app
# Import routes after app is created (avoids circular import)
from app.router import routes
from app.router import project_routes

if __name__ == "__main__":
    app.run(host="localhost", port=5050, debug=True)
    
from app import app
# Import routes after app is created (avoids circular import)
from app.router import routes
from app.router import project_routes

if __name__ == "__main__":
    app.run(host="localhost", port=5050, debug=True)

