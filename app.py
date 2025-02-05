from flask import Flask, render_template, request, redirect, url_for, session, send_file
import sqlite3
import os
import json
from werkzeug.security import generate_password_hash, check_password_hash
from ai_evaluator import evaluate_ppt
from config import DATABASE, UPLOAD_FOLDER, ADMIN_USERNAME, ADMIN_PASSWORD, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

DATABASE = 'database.db'

import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = 'database.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.executescript(open('schema.sql', 'r').read())

        # Check if admin exists
        cursor.execute("SELECT id FROM users WHERE role = 'admin'")
        admin_exists = cursor.fetchone()

        # If no admin exists, create one
        if not admin_exists:
            username = ADMIN_USERNAME
            password = ADMIN_PASSWORD
            hashed_password = generate_password_hash(password)
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, 'admin')", (username, hashed_password))
            conn.commit()

           


@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, password, role FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()

            if user and check_password_hash(user[1], password):
                session['user_id'] = user[0]
                session['role'] = user[2]
                return redirect(url_for('index'))
        
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'role' not in session or session['role'] != 'admin':
        return "Unauthorized", 403

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, 'user')", (username, hashed_password))
            conn.commit()

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users WHERE role='user'")
        users = cursor.fetchall()

    return render_template('admin.html', users=users)

@app.route('/upload', methods=['GET', 'POST'])
def upload_ppt():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        team_name = request.form['team_name']
        problem_id = request.form['problem_id']
        domain = request.form['domain']
        ppt_file = request.files['ppt']

        filename = os.path.join(UPLOAD_FOLDER, ppt_file.filename)
        ppt_file.save(filename)

        scores, flag = evaluate_ppt(filename)

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO teams 
                (team_name, problem_id, domain, ppt_path, relevance, innovation, usefulness, originality, feasibility, future_scope, sustainability, presentation, judges_opinion_score, flag) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (team_name, problem_id, domain, filename, *scores, None, None, flag))
            conn.commit()

        return redirect(url_for('index'))

    return render_template('upload.html')

@app.route('/view/<category>')
def view_category(category):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if category not in ['Red', 'Orange', 'Green']:
        return "Invalid category", 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams WHERE flag=?", (category,))
        teams = cursor.fetchall()

    return render_template('view_category.html', teams=teams, category=category)

@app.route('/move_to_orange/<int:team_id>')
def move_to_orange(team_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE teams SET flag='Orange' WHERE id=?", (team_id,))
        conn.commit()

    return redirect(url_for('view_category', category='Red'))

@app.route('/download/<int:team_id>')
def download_ppt(team_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ppt_path FROM teams WHERE id=?", (team_id,))
        result = cursor.fetchone()

        if result:
            return send_file(result[0], as_attachment=True)

    return "File not found", 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
