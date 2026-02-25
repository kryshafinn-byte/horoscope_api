from flask import jsonify

def make_compatibility(app):
    print("Compatibility routes have been loaded and matched!")

    @app.route('/compatibility/<sign1>/<sign2>', methods=['GET'])
    def get_compatibility(sign1, sign2):
        """
        Returns how two zodiac signs match based on their elements.
        """

        # Zodiac elements
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

        # Compatibility logic
        if e1 == e2:
            level = "High"
            description = "A natural cosmic match — harmony, ease, and shared energy. Time to think of a whimsical pick-up line, I think!"
        elif (e1, e2) in [
            ("fire", "air"), ("air", "fire"),
            ("earth", "water"), ("water", "earth")
        ]:
            level = "Medium"
            description = "There is potential here. Just will take some time..."
        else:
            level = "Low"
            description = "These elements are opposites! Either will make a storm or sparks! Depends on what the stars are whispering..."

        return jsonify({
            "sign1": sign1.capitalize(),
            "sign2": sign2.capitalize(),
            "compatibility": level,
            "description": description
        })
