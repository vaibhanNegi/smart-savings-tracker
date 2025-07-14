# api_server.py
'''
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL database
def get_connection():
    return psycopg2.connect(
        dbname="smart_savings",
        user="postgres",
        password="yourpassword",
        host="localhost",
        port="5432"
    )

@app.route("/add-expense", methods=["POST"])
def add_expense():
    data = request.json
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO expense_data (amount, category, payment_method, day, entry)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        data["amount"], data["category"], data["payment_method"],
        data["day"], data["entry"]
    ))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Expense added successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
'''