import sqlite3

def create_db():
    conn = sqlite3.connect('users.db')  # Connect to the database
    c = conn.cursor()
    # Create the 'users' table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                     username TEXT NOT NULL UNIQUE,
                     password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Call the function
create_db()
