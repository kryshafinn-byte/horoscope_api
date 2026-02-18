from flask import Flask
from config import DB_CONFIG
import mysql.connector
from flasgger import Swagger
from app.routes.signs_routes import signs   # renamed the blueprint to "signs" in signs_routes.py


def make_app():

    app = Flask(__name__)
    Swagger(app)  # Creating Swagger for API documentation

    def get_db_connection():
        return mysql.connector.connect(**DB_CONFIG) #db connection

    app.get_db_connection = get_db_connection #function to get db connection

    app.register_blueprint(signs) #register the blueprint with the app

    return app
