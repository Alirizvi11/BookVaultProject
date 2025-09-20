from flask import Blueprint, request, jsonify
from app.db_config import get_connection
from datetime import datetime

issue_book_bp = Blueprint('issue_book_bp', __name__, url_prefix='/issue_book')

@issue_book_bp.route('/issue-book', methods=['POST'])
def issue_book():
    data = request.get_json()
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # 🔄 Insert transaction (corrected: no expected_return_date column)
        cursor.execute("""
            INSERT INTO transactions (book_id, member_id, issue_date, return_date, status)
            VALUES (?, ?, ?, NULL, ?)
        """, (
            data['book_id'],
            data['member_id'],
            data['issue_date'],
            "Issued"
        ))

        # 📉 Decrease available copies
        cursor.execute("""
            UPDATE books
            SET available_copies = available_copies - 1
            WHERE book_id = ?
        """, (data['book_id'],))

        conn.commit()
        return jsonify({"message": "Book issued successfully"}), 200

    except Exception as e:
        print("❌ IssueBook error:", e)
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
