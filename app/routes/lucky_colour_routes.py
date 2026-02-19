from flask import jsonify

def make_lucky_colours(app):
    print("Lucky colour routes loaded!")


    @app.route('/lucky-colour/<name>', methods=['GET'])
    def get_lucky_colours(name):
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
            "lucky_colours": [result['colour1'],result['colour2'],result['colour3']]
        })
