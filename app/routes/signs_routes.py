from flask import Blueprint, jsonify, current_app
signs_bp = Blueprint("signs", __name__)

@signs_bp.route("/signs", methods=["GET"])
def get_signs():
    db = current_app.get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM signs")
    signs = cursor.fetchall()

    cursor.close()
    db.close()
    return jsonify(signs)