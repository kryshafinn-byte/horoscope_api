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

    # create the app
    app = Flask(__name__)

    # add swagger docs
    Swagger(app)

    # gets the database connection
    def get_db_connection():
        print("Preparing database connection...")

        settings = DB_CONFIG.copy()
        if "host" not in settings:
            print("Warning: host is missing from DB config.")
        else:
            if settings.get("user") is None:
                print("Warning: user is missing from DB config.")
        try:
            conn = mysql.connector.connect(**settings)
            print("Database connection successful.")
            return conn
        except Exception as e:
            print("Database connection failed:", e)
            return None

    # attaches the helper to the app
    app.get_db_connection = get_db_connection

    # register the routes
    print("Registering routes...")
    app.register_blueprint(signs)
    make_lucky_colours(app)
    make_compatibility(app)

    print("App setup complete.")
    return app