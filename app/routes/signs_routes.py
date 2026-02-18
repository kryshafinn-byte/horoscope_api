from flask import Blueprint, jsonify, current_app, request
from app.models.fire_signs import FireSign
from app.models.earth_signs import EarthSign
from app.models.air_signs import AirSign
from app.models.water_signs import WaterSign
from datetime import datetime
from app.utils.sign_calculator import get_sign_from_date


signs = Blueprint("signs", __name__)

@signs.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to my Horoscopes API"})


@signs.route("/signs", methods=["GET"])
def get_signs():
    db = current_app.get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM signs")
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    signs = []

    for row in rows:
        element = row["element"]
        sign = None

        if element == "Fire":
            sign = FireSign(row["name"], row["date_range"], element)
        elif element == "Earth":
            sign = EarthSign(row["name"], row["date_range"], element)
        elif element == "Air":
            sign = AirSign(row["name"], row["date_range"], element)
        elif element == "Water":
            sign = WaterSign(row["name"], row["date_range"], element)

        if sign:
            signs.append(sign.as_json())

@signs.route('/signs/<name>', methods=['GET'])
def get_the_sign_name(name):
    db = current_app.get_db_connection()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM signs WHERE LOWER(name) = LOWER(%s)"
    cursor.execute(query,(name,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "The stars have not crossed as your sign cannot be found!"}), 404

@signs.route("/signs/by-date", methods=["GET"])
def get_sign_by_date():
    birthdate = request.args.get("date")
    print("Birthdate received:", birthdate)

    if not birthdate:
        print("Error: No date has been provided for the stars to align with.")
        return jsonify({"error": "Missing date for the stars to align with!"}), 400
    try:
        date_obj = datetime.strptime(birthdate, "%Y-%m-%d")
        print("Date now locked in and created:", date_obj)
    except ValueError:
        print("Error: Seems that those dates are beyond this universe:", birthdate)
        return jsonify({"error": "Uh oh! Seems that those dates are beyond this universe. Manifesting for you to use YYYY-MM-DD"}), 400

    sign_name = get_sign_from_date(date_obj)
    print("Sign returned by get_sign_from_date:", sign_name)

    db = current_app.get_db_connection()
    cursor = db.cursor(dictionary=True)
    print("Double checking the stars for your sign:", sign_name)

    cursor.execute("SELECT * FROM signs WHERE LOWER(name) = LOWER(%s)", (sign_name,))
    result = cursor.fetchone()

    cursor.close()
    db.close()

    print("The stars have your results:", result)

    if result:
        print("Shooting stars! Your sign has emerged from the cosmic database:", result)
        return jsonify(result), 200
    else:
        print("Error: Stars have been shot but your sign has not emerged from the cosmic database:", sign_name)
        return jsonify({"error": "Sign has flown too high and cannot be found..."}), 404

    return jsonify(signs)
