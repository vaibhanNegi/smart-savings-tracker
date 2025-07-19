import email
import psycopg2
import psycopg2.extras

# Connect to PostgreSQL
def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="smart_saving_db",
        user="postgres",
        password="1234",
        port="5432"
    )

# Create users table
def create_user_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Insert a new user
def insert_user(username, email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s);", (username, email, password))
    conn.commit()
    cursor.close()
    conn.close()

# Login check
def login_user(username, email, password):
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username = %s AND email = %s AND password = %s;"
    cursor.execute(query, (username, email, password))
    
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return user

