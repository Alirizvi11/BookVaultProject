from flask import Blueprint, jsonify
from app.db_config import get_connection

analytics_bp = Blueprint('analytics_bp', __name__, url_prefix='/analytics')

@analytics_bp.route('/get-analytics', methods=['GET'])
def get_analytics():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Overdue books (not returned)
        cursor.execute("SELECT COUNT(*) FROM transactions WHERE return_date IS NULL")
        overdue = cursor.fetchone()[0]

        # Most popular book (highest issue count)
        cursor.execute("""
            SELECT title FROM books
            WHERE book_id IN (
                SELECT book_id FROM transactions
                GROUP BY book_id
                ORDER BY COUNT(*) DESC
            ) FETCH FIRST 1 ROWS ONLY
        """)
        result = cursor.fetchone()
        popular = result[0] if result else "N/A"


        # Active members (who issued at least one book)
        cursor.execute("SELECT COUNT(DISTINCT member_id) FROM transactions")
        active_members = cursor.fetchone()[0]

        return jsonify({
            "overdue_books": overdue,
            "most_popular": popular,
            "active_members": active_members
        })
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()
