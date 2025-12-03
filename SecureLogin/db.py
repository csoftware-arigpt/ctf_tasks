import sqlite3

conn = None

def get_db():
    global conn
    if conn is None:
        conn = sqlite3.connect(':memory:', check_same_thread=False)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY, 
                username TEXT, 
                password TEXT, 
                role TEXT
            )
        ''')
        
        cursor.execute("INSERT INTO users (username, password, role) VALUES ('admin', 'SUp3r_C0mpl3x_P4ss', 'admin')")
        cursor.execute("INSERT INTO users (username, password, role) VALUES ('guest', 'guest', 'user')")
        conn.commit()
    return conn