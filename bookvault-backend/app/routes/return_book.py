from flask import Blueprint, request, jsonify
from app.db_config import get_connection

return_book_bp = Blueprint('return_book_bp', __name__, url_prefix='/return_book')

@return_book_bp.route('/return-book', methods=['POST'])
def return_book():
    data = request.json
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.callproc("RETURN_BOOK_PROC", [data['txn_id']])
        conn.commit()
        return jsonify({"message": "Book returned successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()
