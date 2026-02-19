from flask import jsonify

def make_lucky_colours(app):
    print("Lucky colour routes loaded!")

    @app.route('/lucky-colour/<name>', methods=['GET'])
    def get_lucky_colours(name):
        """
        Get Lucky Colours for your Zodiac Sign (or someone else's!)
        ---
        tags:
          - Lucky Colours
        parameters:
          - name: name
            in: path
            type: string
            required: true
            description: The zodiac sign to look up
        responses:
          200:
            description: A list of lucky colours for the given sign
            examples:
              application/json:
                {
                  "sign": "Aries",
                  "lucky_colours": ["Red", "Scarlet", "Fire Orange"]
                }
          404:
            description: Sign not found
            examples:
              application/json:
                {"error": "Stars can't find those lucky colours of yours!"}
        """
        db = app.get_db_connection()
        cursor = db.cursor(dictionary=True)

        query = """
            SELECT colour1, colour2, colour3
            FROM lucky_colours
            WHERE LOWER(sign_name) = LOWER(%s)
        """
        cursor.execute(query, (name,))
        result = cursor.fetchone()

        if not result:
            return jsonify({"error": "Stars can't find those lucky colours of yours!"}), 404

        return jsonify({
            "sign": name.capitalize(),
            "lucky_colours": [
                result['colour1'],
                result['colour2'],
                result['colour3']
            ]
        })