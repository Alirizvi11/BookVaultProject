from flask import Blueprint, jsonify
from app.db_config import get_connection
  # Assuming you have these

book_bp = Blueprint("book_bp", __name__, url_prefix="/books")

@book_bp.route("/get-books")
def get_books():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT book_id, title, author, genre, available_copies, cover_url
    FROM books
""")
    rows = cursor.fetchall()
    books = []
    for row in rows:
       books.append({
    "book_id": row[0],
    "title": row[1],
    "author": row[2],
    "genre": row[3],
    "available": row[4],  # ✅ This maps to available_copies
    "cover_url": row[5] or ""
})

    cursor.close()
    conn.close()
    return jsonify(books)
