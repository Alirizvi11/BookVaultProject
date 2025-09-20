from flask import Blueprint, request, jsonify
from app.db_config import get_connection


return_book_bp = Blueprint('return_book_bp', __name__, url_prefix='/return_book')

@return_book_bp.route('/return-book', methods=['POST'])
def return_book():
    data = request.get_json()
    txn_id = data.get('txn_id')

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # 🔍 Get book_id from transaction
        cursor.execute("SELECT book_id FROM transactions WHERE txn_id = ?", (txn_id,))
        result = cursor.fetchone()

        if not result:
            return jsonify({"error": "Transaction not found"}), 404

        book_id = result[0]

        # 📅 Update return_date to today
        cursor.execute("""
            UPDATE transactions
            SET return_date = DATE('now')
            WHERE txn_id = ?
        """, (txn_id,))

        # 📈 Increment available copies
        cursor.execute("""
            UPDATE books
            SET available_copies = available_copies + 1
            WHERE book_id = ?
        """, (book_id,))

        conn.commit()
        return jsonify({"message": "Book returned successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()
