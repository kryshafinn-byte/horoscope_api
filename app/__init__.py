from flask import Flask
from config import DB_CONFIG
import mysql.connector

def make_app():
    app = Flask(__name__)

    #db connection
    def get_db_connection():
        return mysql.connector.connect (**DB_CONFIG)
    
    #Wanting the db to be open to rest of the app
    app.get_db_connection = get_db_connection

    #Getting my blueprint routes to connect to my url path
    from app.routes.signs_routes import signs_bp
    app.regisrer_blueprint(signs_bp)

    return app
