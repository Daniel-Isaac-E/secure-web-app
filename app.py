from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt
import re

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ---------------- DATABASE ----------------
def get_db():
    return sqlite3.connect("database.db")

def init_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT UNIQUE,
            password BLOB,
            role TEXT
        )
    """)
    db.commit()
    db.close()

init_db()

# ---------------- PASSWORD POLICY ----------------
def valid_password(password):
    return (
        len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*]", password)
    )

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return redirect("/login")

# ---------- SIGNUP ----------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if not valid_password(password):
            return "Password too weak (min 8 chars, upper, lower, number, symbol)"

        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO users VALUES (NULL, ?, ?, ?, ?)",
                (username, email, hashed, "user")
            )
            db.commit()
            db.close()
            return redirect("/login")
        except:
            return "Email already exists"

    return render_template("signup.html")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "SELECT id, password, role FROM users WHERE email = ?",
            (email,)
        )
        user = cursor.fetchone()
        db.close()

        if user and bcrypt.checkpw(password.encode(), user[1]):
            session["user_id"] = user[0]
            session["role"] = user[2]
            return redirect("/dashboard")
        else:
            return "Invalid email or password"

    return render_template("login.html")

# ---------- USER DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("dashboard.html", role=session["role"])

# ---------- ADMIN DASHBOARD ----------
@app.route("/admin")
def admin():
    if "user_id" not in session or session["role"] != "admin":
        return render_template("unauthorized.html")
    return render_template("admin.html")

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
