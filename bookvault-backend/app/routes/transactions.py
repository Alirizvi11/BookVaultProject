from flask import Blueprint, request, jsonify, make_response
from app.db_config import get_connection


transactions_bp = Blueprint('transactions_bp', __name__, url_prefix='/transactions')

@transactions_bp.route('/get-transactions', methods=['GET'])
def get_transactions():
    date = request.args.get('date')  # Format: '2025-09-06'
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT txn_id, book_id, member_id, issue_date, return_date, fine
            FROM transactions
            WHERE DATE(issue_date) = ?
        """, (date,))
        rows = cursor.fetchall()

        txns = [{
            "txn_id": r[0],
            "book_id": r[1],
            "member_id": r[2],
            "issue_date": str(r[3]),
            "return_date": str(r[4]) if r[4] else None,
            "fine": r[5]
        } for r in rows]

        return jsonify(txns), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# ✅ Export transactions by date (CSV download)
@transactions_bp.route('/export-transactions-csv', methods=['GET'])
def export_transactions_csv():
    date = request.args.get('date')
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT txn_id, book_id, member_id, issue_date, return_date, fine
            FROM transactions
            WHERE DATE(issue_date) = ?
        """, (date,))
        rows = cursor.fetchall()

        csv_data = "txn_id,book_id,member_id,issue_date,return_date,fine\n"
        for r in rows:
            csv_data += f"{r[0]},{r[1]},{r[2]},{r[3]},{r[4]},{r[5]}\n"

        response = make_response(csv_data)
        response.headers["Content-Disposition"] = f"attachment; filename=transactions_{date}.csv"
        response.headers["Content-Type"] = "text/csv"
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@transactions_bp.route('/get-overdue-transactions', methods=['GET'])
def get_overdue_transactions():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT txn_id, book_id, member_id, issue_date, return_date, fine
            FROM transactions
            WHERE return_date IS NULL AND issue_date < DATE('now', '-14 days')
        """)
        rows = cursor.fetchall()

        txns = [{
            "txn_id": r[0],
            "book_id": r[1],
            "member_id": r[2],
            "issue_date": str(r[3]),
            "return_date": str(r[4]) if r[4] else None,
            "fine": r[5]
        } for r in rows]

        return jsonify(txns), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@transactions_bp.route('/get-member-transactions', methods=['GET'])
def get_member_transactions():
    member_id = request.args.get('member_id')
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT txn_id, book_id, issue_date, return_date, fine
            FROM transactions
            WHERE member_id = ?
            ORDER BY issue_date DESC
        """, (member_id,))
        rows = cursor.fetchall()

        txns = [{
            "txn_id": r[0],
            "book_id": r[1],
            "issue_date": str(r[2]),
            "return_date": str(r[3]) if r[3] else None,
            "fine": r[4]
        } for r in rows]

        return jsonify(txns), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# 📝 Placeholder route (already handled in issue_book.py)
@transactions_bp.route('/issue-book', methods=['POST'])
def issue_book():
    return jsonify({"message": "Book issued successfully"}), 200
