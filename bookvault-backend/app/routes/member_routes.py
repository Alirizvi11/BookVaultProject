from flask import Blueprint, request, jsonify
from app.db_config import get_connection


member_bp = Blueprint('member_bp', __name__, url_prefix='/members')

@member_bp.route('/register-member', methods=['POST'])
def register_member():
    data = request.get_json()
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
    INSERT INTO members (name, email, phone, address, joined_on)
    VALUES (?, ?, ?, ?, DATE('now'))
""", (
    data.get("name"),
    data.get("email"),
    data.get("phone"),
    data.get("address", "")
))


        conn.commit()
        return jsonify({"message": "Member registered successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()

@member_bp.route('/get-members', methods=['GET'])
def get_members():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT member_id, name, email, phone FROM members")
        rows = cursor.fetchall()

        members = [
            {
                "member_id": r[0],
                "name": r[1],
                "email": r[2],
                "phone": r[3]
            } for r in rows
        ]

        return jsonify(members), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()
