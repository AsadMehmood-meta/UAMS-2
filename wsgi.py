<<<<<<< HEAD
from app import app
# Import routes after app is created (avoids circular import)
from app.router import routes
from app.router import project_routes

if __name__ == "__main__":
    app.run(host="localhost", port=5050, debug=True)
=======
from app import app
# Import routes after app is created (avoids circular import)
from app.router import routes
from app.router import project_routes

if __name__ == "__main__":
    app.run(host="localhost", port=5050, debug=True)
>>>>>>> 7ca1db230b61a2d4bb7786040d65f0c1ea2d49b3
