import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('political_characters.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create a table for political characters
cursor.execute('''
CREATE TABLE IF NOT EXISTS Characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    party TEXT NOT NULL,
    position TEXT NOT NULL
)
''')

# Function to add a political character
def add_character(name, party, position):
    cursor.execute('''INSERT INTO Characters (name, party, position)
                      VALUES (?, ?, ?)''', (name, party, position))
    conn.commit()

# Function to retrieve all characters
def get_all_characters():
    cursor.execute('SELECT * FROM Characters')
    return cursor.fetchall()

# Function to close the database connection
def close_connection():
    conn.close()