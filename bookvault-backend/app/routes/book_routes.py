from flask import Blueprint, jsonify
from app.db_config import get_connection

book_bp = Blueprint("book_bp", __name__, url_prefix="/books")

@book_bp.route("/get-books", methods=["GET"])
def get_books():
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT book_id, title, author, genre, available_copies, cover_url
            FROM books
        """)
        rows = cursor.fetchall()

        books = [
            {
                "book_id": row[0],
                "title": row[1],
                "author": row[2],
                "genre": row[3],
                "available": row[4],
                "cover_url": row[5] or ""
            }
            for row in rows
        ]

        return jsonify(books)

    except Exception as e:
        print("❌ GetBooks error:", e)
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
