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
    """
    Creates the Flask app and sets up everything it needs.
    """
    print("Starting up the horoscope API...")

    app = Flask(__name__)

    # Swagger setup
    swagger_config = {
        "title": "Horoscope API",
        "uiversion": 3,
        "description": "A friendly little API for zodiac signs, lucky colours, and compatibility.",
    }
    Swagger(app, config=swagger_config)

    # database connection helper
    def get_db_connection():
        """
        Creates a MySQL connection using the settings in config.py.
        Returns a live connection or None if something goes wrong.
        """
        print("Preparing database connection...")

        settings = DB_CONFIG.copy()

        try:
            conn = mysql.connector.connect(**settings)
            print("Database connection successful.")
            return conn
        except Exception as e:
            print("Database connection failed:", e)
            return None

    app.get_db_connection = get_db_connection

    # register routes
    print("Registering routes...")
    app.register_blueprint(signs)
    make_lucky_colours(app)
    make_compatibility(app)

    print("App setup complete.")
    return app
