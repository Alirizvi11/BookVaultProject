from flask import Flask
from flask_cors import CORS

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

# ✅ Force CORS headers for all routes
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# 📦 Register all Blueprints
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

@app.route("/api/update-cover", methods=["POST"])
def update_cover():
    data = request.get_json()
    title = data.get("title")
    cover_url = data.get("cover_url")

    cursor.execute("""
    UPDATE books
    SET cover_url = :cover_url
    WHERE LOWER(title) LIKE LOWER(:title)
""", {"cover_url": cover_url, "title": f"%{title}%"})

    conn.commit()
    return jsonify({"message": "Cover updated"}), 200


# 🏁 Start the server on 127.0.0.1:5000
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
