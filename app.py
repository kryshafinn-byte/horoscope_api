from flask import Flask, jsonify
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

def get_database_link():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/signs", methods=["GET"])
def get_signs():
    db = get_database_link()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM signs")
    signs = cursor.fetchall()

    cursor.close()
    db.close()
    return jsonify(signs)

if __name__ == "__main__":
    app.run(debug=True)