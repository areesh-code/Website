from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Initialize the database
def init_db():
    if not os.path.exists("users.db"):
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        conn.commit()
        conn.close()

init_db()

# Home page (redirects to login)
@app.route('/')
def home():
    return render_template("login.html")

# Handle login
@app.route('/login', methods=["POST"])
def check_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"success": False, "message": "Please fill all fields!"})

    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cur.fetchone()
    conn.close()

    if user:
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "This email or password is wrong. Please try again."})

# Handle signup
@app.route('/signup', methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"success": False, "message": "Please fill all fields!"})

    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Registered successfully!"})
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"success": False, "message": "Username already exists!"})

if __name__ == "__main__":
    app.run(debug=True)