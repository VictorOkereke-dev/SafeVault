import sqlite3

def get_db_connection():
    conn = sqlite3.connect('safevault.db')
    conn.row_factory = sqlite3.Row
    return conn

def query_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user
  
