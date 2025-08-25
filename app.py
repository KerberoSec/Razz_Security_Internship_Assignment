from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Create users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0
        )
    ''')
    
    # Insert sample data
    try:
        c.execute("INSERT INTO users (username, password, is_admin) VALUES ('admin', 'RAZZ{sql1_bYP4sS_MAst3r}', 1)")
        c.execute("INSERT INTO users (username, password, is_admin) VALUES ('john_doe', 'password123', 0)")
        c.execute("INSERT INTO users (username, password, is_admin) VALUES ('jane_smith', 'securepass', 0)")
        conn.commit()
    except sqlite3.IntegrityError:
        # Records already exist
        pass
        
    conn.close()

# Vulnerable login function
def check_login(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # VULNERABLE SQL QUERY - susceptible to injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    try:
        c.execute(query)
        user = c.fetchone()
    except sqlite3.Error as e:
        return None, str(e)
    
    conn.close()
    
    if user:
        return {
            'id': user[0],
            'username': user[1],
            'is_admin': bool(user[3])
        }, None
    else:
        return None, "Invalid credentials"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    
    user, error = check_login(username, password)
    
    if user:
        response_data = {
            'success': True,
            'username': user['username'],
            'is_admin': user['is_admin']
        }
        
        if user['is_admin']:
            # Get the admin password (flag) from the database
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute("SELECT password FROM users WHERE username = 'admin'")
            admin_password = c.fetchone()[0]
            conn.close()
            
            response_data['flag'] = admin_password
            
        return jsonify(response_data)
    else:
        return jsonify({
            'success': False,
            'message': error or 'Invalid credentials'
        })

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
