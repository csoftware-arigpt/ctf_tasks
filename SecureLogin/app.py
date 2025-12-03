from flask import Flask, request, render_template
from config import Config
from db import get_db
from waf import check_payload

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    if not check_payload(username) or not check_payload(password):
        return render_template('index.html', message="<h3 style='color:red'>⚠️ THREAT DETECTED</h3><p>WAF blocked malicious input.</p>")

    try:
        conn = get_db()
        cursor = conn.cursor()
        
        query = f"SELECT id, username, role FROM users WHERE username = '{username}' AND password = '{password}'"
        
        cursor.execute(query)
        user = cursor.fetchone()

        if user:
            role = user[2]
            if role == 'admin':
                success_msg = f"<h2 style='color:#00ffc8'>ACCESS GRANTED</h2><hr><p>Welcome, Admin.</p><p style='border:1px solid; padding:10px'>{app.config['FLAG']}</p>"
                return render_template('index.html', message=success_msg)
            else:
                return render_template('index.html', message=f"<h3 style='color:orange'>Welcome, {user[1]}</h3><p>Insufficient privileges for flag.</p>")
        else:
            return render_template('index.html', message="<h3 style='color:red'>❌ ACCESS DENIED</h3><p>Invalid username or password.</p>")

    except Exception as e:
        return render_template('index.html', message=f"<h3 style='color:red'>💥 SYSTEM ERROR</h3><p>SQL Syntax Error.</p>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)