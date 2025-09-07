from flask import Blueprint, request, jsonify, make_response

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

@admin_bp.route('/admin-login', methods=['POST'])
def admin_login():
    data = request.get_json()
    # Dummy check for now
    if data["username"] == "BOOKVAULT_USER" and data["password"] == "b1":
        response = make_response(jsonify({"status": "success"}), 200)
    else:
        response = make_response(jsonify({"status": "failed"}), 401)

    # ✅ Add CORS headers manually
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    return response
