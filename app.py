from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret123'  # Used for session management and flash messages

# Dummy login credentials
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            return "✅ Login Successful! Welcome, admin!"
        else:
            flash('❌ Invalid username or password. Try again.')
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

