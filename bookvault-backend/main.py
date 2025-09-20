from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

# 🔗 Import all route Blueprints
from app.routes.issue_book import issue_book_bp
from app.routes.return_book import return_book_bp
from app.routes.transactions import transactions_bp
from app.routes.admin_login import admin_bp
from app.routes.book_routes import book_bp
from app.routes.member_routes import member_bp
from app.routes.analytics import analytics_bp

# 🚀 Initialize Flask app
app = Flask(__name__)

# 🗃️ Initialize SQLite connection
conn = sqlite3.connect('bookvault.db', check_same_thread=False)
cursor = conn.cursor()

# ✅ Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# 📦 Register Blueprints
app.register_blueprint(issue_book_bp)
app.register_blueprint(return_book_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(book_bp)
app.register_blueprint(member_bp)
app.register_blueprint(analytics_bp)

# ✅ Health check route
@app.route('/')
def home():
    return "📚 BookVault Backend is Running ✅"

# 🖼️ Cover update route
@app.route("/api/update-cover", methods=["POST"])
def update_cover():
    data = request.get_json()
    title = data.get("title")
    cover_url = data.get("cover_url")

    try:
        cursor.execute("""
            UPDATE books
            SET cover_url = ?
            WHERE LOWER(title) LIKE LOWER(?)
        """, (cover_url, f"%{title}%"))
        conn.commit()
        return jsonify({"message": "Cover updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🏁 Start the server
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
