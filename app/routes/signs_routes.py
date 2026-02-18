from flask import Blueprint, jsonify, current_app
from app.models.fire_signs import FireSign
from app.models.earth_signs import EarthSign
from app.models.air_signs import AirSign
from app.models.water_signs import WaterSign

signs_bp = Blueprint("signs", __name__)

@signs_bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to my Horoscopes API"})


@signs_bp.route("/signs", methods=["GET"])
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

@signs_bp.route('/signs/<name>', methods=['GET'])
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

    return jsonify(signs)
