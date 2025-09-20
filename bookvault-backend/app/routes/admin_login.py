from flask import Blueprint, request, jsonify, make_response
from app.db_config import get_connection

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

@admin_bp.route('/admin-login', methods=['POST'])
def admin_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM admins WHERE username = ? AND password = ?", (username, password))
    admin = cursor.fetchone()

    if admin:
        response = make_response(jsonify({"status": "success"}), 200)
    else:
        response = make_response(jsonify({"status": "failed"}), 401)

    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    return response
