print("LOADED: signs_routes.py")
"""
Routes for the Horoscope API.
"""
from flask import Blueprint, jsonify, current_app, request
from app.models.fire_signs import FireSign
from app.models.earth_signs import EarthSign
from app.models.air_signs import AirSign
from app.models.water_signs import WaterSign
from datetime import datetime
from app.utils.sign_calculator import SignCalculator

signs = Blueprint("signs", __name__)

@signs.route("/", methods=["GET"])
def home():
    """
    A little homepage welcome from the Horoscope API.
    ---
    description: A little homepage welcome from the Horoscope API.
    """
    return jsonify({"message": "Welcome to my Horoscopes API"})


@signs.route("/signs", methods=["GET"])
def get_signs():
    """
    Get every zodiac sign from the database.
    ---
    description: Get every zodiac sign from the database.
    """
    db = current_app.get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM signs")
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    signs_list = []

    for row in rows:
        element = row["element"]

        if element == "Fire":
            sign = FireSign(row["name"], row["date_range"], element)
        elif element == "Earth":
            sign = EarthSign(row["name"], row["date_range"], element)
        elif element == "Air":
            sign = AirSign(row["name"], row["date_range"], element)
        elif element == "Water":
            sign = WaterSign(row["name"], row["date_range"], element)
        else:
            sign = None

        if sign:
            signs_list.append(sign.as_json())

    return jsonify(signs_list), 200

@signs.route("/signs/by-date", methods=["GET"])
def get_sign_by_date():
    """
    Work out your zodiac sign from your birthdate.
    ---
    description: Work out your zodiac sign from your birthdate.
    """
    date_str = request.args.get("date")

    if not date_str:
        return jsonify({"error": "Please provide a date in YYYY-MM-DD format"}), 400

    try:
        sign = SignCalculator.from_string(date_str)
    except ValueError as err:
        return jsonify({"error": str(err)}), 400

    return jsonify({"sign": sign}), 200

@signs.route('/signs/<name>', methods=['GET'])
def get_the_sign_name(name):
    """
    Find a zodiac sign by name.
    ---
    description: Find a zodiac sign by name.
    """
    db = current_app.get_db_connection()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM signs WHERE LOWER(name) = LOWER(%s)"
    cursor.execute(query, (name,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "The stars have not crossed as your sign cannot be found!"}), 404