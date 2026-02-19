from flask import Flask
from config import DB_CONFIG
import mysql.connector
from flasgger import Swagger
from app.routes.signs_routes import signs
from app.routes.lucky_colour_routes import make_lucky_colours

def make_app():

    app = Flask(__name__)
    Swagger(app)

    def get_db_connection():
        return mysql.connector.connect(**DB_CONFIG)

    app.get_db_connection = get_db_connection #getting the db connection

    app.register_blueprint(signs) #registering the blueprint
    make_lucky_colours(app)

    return app
