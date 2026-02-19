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
    try:
        birthdate = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    month = birthdate.month
    day = birthdate.day
    zodiac_dates = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21)),
    ]

    for sign, start, end in zodiac_dates:
        start_month, start_day = start
        end_month, end_day = end

        if (month == start_month and day >= start_day) or \
           (month == end_month and day <= end_day):
            return jsonify({"sign": sign})

    return jsonify({"error": "Could not determine zodiac sign"}), 500


@signs.route('/signs/<name>', methods=['GET'])
def get_the_sign_name(name):
    """
    Look up a zodiac sign by name — because sometimes you just want to have a good nose around.
    ---
    summary: Get a specific zodiac sign
    description: >
      Type in the name of a zodiac sign and I'll fetch its details for you.
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: The name of the zodiac sign you want info on
        example: "Leo"
    responses:
      200:
        description: Found the sign you're looking for
        examples:
          application/json:
            name: "Leo"
            element: "Fire"
            date_range: "July 23 - August 22"
      404:
        description: >
          Could not find that sign. Either it doesn't exist or you typed it
          in wrong.
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