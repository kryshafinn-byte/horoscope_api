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
    A warm and whimsical welcome to the Horoscope API. The stars have whispered to me to expect you!
    ---
    summary: Say hello to the API
    description: >
      Just a hello so you know the server is here, and ready to look up your star sign choices.
    responses:
      200:
        description: The API is here and is politely waiting to help you discover your star sign!
        examples:
          application/json:
            message: "Welcome to my Horoscopes API"
    """
    return jsonify({"message": "Welcome to my Horoscopes API"})


@signs.route("/signs", methods=["GET"])
def get_signs():
    """
    Fetch the full lineup of zodiac signs — the whole starry-eyed bunch.
    ---
    summary: Get all zodiac signs
    description: >
      Returns every zodiac sign stored in the database. 
      Great if you want to browse, compare, or teach yourself about them all equally.
    responses:
      200:
        description: Successfully retrieved all signs
        examples:
          application/json:
            - name: "Aries"
              element: "Fire"
              date_range: "March 21 - April 19"
            - name: "Taurus"
              element: "Earth"
              date_range: "April 20 - May 20"
    """

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

    return jsonify(signs), 200


@signs.route("/signs/by-date", methods=["GET"])
def get_sign_by_date():
    """
    Figure out what zodiac sign your birthdate actually belongs to.
    ---
    summary: Reveal your zodiac sign (without needing to consult the stars yourself)
    description: >
      Pop in your birthdate and I'll travel to the stars to grab it. No moon charts, no
      crystal balls — just clean logic and a bit of fun!
    parameters:
      - name: date
        in: query
        type: string
        required: true
        description: >
          Your birthdate in the classic YYYY-MM-DD format. 
          (If you send me anything else, the stars will complain.)
        example: "1999-12-31"
    responses:
      200:
        description: Your zodiac sign has been successfully identified
        examples:
          application/json:
            name: "Leo"
            element: "Fire"
            date_range: "July 23 - August 22"
      400:
        description: >
          Something went wrong — try again with a valid date in YYYY-MM-DD format.
      404:
        description: >
          I tried, I really did, but your sign isn't in the stars, nor maybe this world. 
            (Or maybe you were born on a day when the stars were not aligned!)
    """
    from datetime import datetime
    from flask import request, jsonify

    date_str = request.args.get("date")

    if not date_str:
        return jsonify({"error": "Please provide a date in YYYY-MM-DD format"}), 400
@signs.route("/signs/by-date", methods=["GET"])
def get_sign_by_date():
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
  Finds Zodiac sign by name.
  When it is found, it will give the sign name, element, and the date range!
  If the sign is not found, it will return an error message.
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