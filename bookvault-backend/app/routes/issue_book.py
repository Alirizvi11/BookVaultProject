from flask import Blueprint, request, jsonify
from app.db_config import get_connection

issue_book_bp = Blueprint('issue_book_bp', __name__,url_prefix='/issue_book')

@issue_book_bp.route('/issue-book', methods=['POST'])
def issue_book():
    data = request.get_json()
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # ✅ Call stored procedure with 4 arguments
        cursor.callproc("ISSUE_BOOK_PROC", [
            data['book_id'],
            data['member_id'],
            data['issue_date'],
            data['expected_return_date']
        ])

        conn.commit()
        return jsonify({"message": "Book issued successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
