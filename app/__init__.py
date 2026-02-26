"""
Makes the Flask app for my horoscope API.
Trying to keep things tidy and readable.
"""

from flask import Flask
from config import DB_CONFIG
import mysql.connector
from flasgger import Swagger

# route imports
from app.routes.signs_routes import signs
from app.routes.lucky_colour_routes import make_lucky_colours
from app.routes.compatibility_routes import make_compatibility

def make_app():
    print("Starting up the horoscope API...")

    app = Flask(__name__)

    # database connection helper
    def get_db_connection():
        settings = DB_CONFIG.copy()
        try:
            return mysql.connector.connect(**settings)
        except Exception as e:
            print("Database connection failed:", e)
            return None

    app.get_db_connection = get_db_connection

    # register routes
    print("Doing the routes...")
    app.register_blueprint(signs)
    make_lucky_colours(app)
    make_compatibility(app)

    # Swagger docs
    Swagger(app)
    print("Swagger template:", app.config.get("SWAGGER"))

    print("App setup complete and ready to find horoscopes!")
    print(app.url_map)
    return app 
