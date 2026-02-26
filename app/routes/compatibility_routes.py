print("LOADED: compatibility_routes.py")

"""
Routes for the Horoscope API.
"""

from flask import jsonify

def make_compatibility(app):
    print("Compatibility routes have been loaded and matched!")

    @app.route('/compatibility/<sign1>/<sign2>', methods=['GET'])
    def get_compatibility(sign1, sign2):
        """
Check if two zodiac signs are a match.
---
description: Check if two zodiac signs are a match.
parameters:
  - name: sign1
    in: path
    type: string
    required: true
    description: The first zodiac sign.
  - name: sign2
    in: path
    type: string
    required: true
    description: The second zodiac sign.
"""


        elements = {
            "aries": "fire", "leo": "fire", "sagittarius": "fire",
            "taurus": "earth", "virgo": "earth", "capricorn": "earth",
            "gemini": "air", "libra": "air", "aquarius": "air",
            "cancer": "water", "scorpio": "water", "pisces": "water"
        }

        s1 = sign1.lower()
        s2 = sign2.lower()

        if s1 not in elements or s2 not in elements:
            return jsonify({"error": "The stars don't recognise one of those signs!"}), 404

        e1 = elements[s1]
        e2 = elements[s2]

        if e1 == e2:
            level = "High"
            description = "A natural cosmic match — harmony and shared energy."
        elif (e1, e2) in [
            ("fire", "air"), ("air", "fire"),
            ("earth", "water"), ("water", "earth")
        ]:
            level = "Medium"
            description = "There’s potential here, just needs a little time."
        else:
            level = "Low"
            description = "Opposite elements — could be sparks or storms."

        return jsonify({
            "sign1": sign1.capitalize(),
            "sign2": sign2.capitalize(),
            "compatibility": level,
            "description": description
        })
