from flask import Flask, render_template, request, send_file, redirect, url_for, session
import pandas as pd
from nifty_value_strategy import run_value_strategy
import sqlite3

app = Flask(__name__)
app.secret_key = 'this_is_a_dev_key'  # Required for session handling

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return redirect(url_for('login'))
        except:
            return "Username already exists."
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    stocks = None
    if request.method == 'POST':
        capital = float(request.form['capital'])
        run_value_strategy(capital)
        df = pd.read_excel('value_strategy_results.xlsx')
        stocks = df.to_dict(orient='records')
    return render_template('dashboard.html', stocks=stocks)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/download')
def download():
    return send_file('value_strategy_results.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
