import sqlite3
from werkzeug.security import generate_password_hash

# Connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Insert users
users = [
    ('user1', generate_password_hash('password1')),  # Replace with your desired username/password
    ('user2', generate_password_hash('password2'))   # Replace with your desired username/password
]

try:
    c.executemany('INSERT INTO users (username, password) VALUES (?, ?)', users)
    conn.commit()
    print("Users added successfully!")
except sqlite3.IntegrityError as e:
    print(f"Error: {e}")
finally:
    conn.close()
