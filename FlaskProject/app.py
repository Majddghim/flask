from flask import Flask, request, render_template, redirect, url_for
import sqlite3

from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
@app.route('/')
def index():
    return redirect(url_for('login'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the database and verify user
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT password FROM users WHERE username = ?', (username,))
        result = c.fetchone()  # Fetch one matching record
        conn.close()

        if result:
            # Check if the password matches
            hashed_password = result[0]
            if check_password_hash(hashed_password,password ):
                return redirect(url_for('users'))  # Redirect to the users page if valid
            else:
                return 'Invalid username or password'
        else:
            return 'Invalid username or password'

    return render_template('login.html')


# Users page (example route)
@app.route('/users')
def users():
    # Fetch all users from the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT username FROM users')  # Fetch all usernames
    all_users = c.fetchall()  # Returns a list of tuples [(user1,), (user2,), ...]
    conn.close()

    # Render the list of users
    return render_template('users.html', users=[user[0] for user in all_users])

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/delete_user/<username>', methods=['POST'])
def delete_user(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    conn.close()
    return redirect(url_for('users'))

if __name__ == '__main__':
    app.run(debug=True)
