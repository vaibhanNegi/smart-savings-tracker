import bcrypt
from db import get_conn

def hash_password(plain):
    return bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode()

def verify_password(plain, hashed):
    return bcrypt.checkpw(plain.encode(), hashed.encode())

def register_user(username, email, password):
    hashed = hash_password(password)
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id;",
                (username, email, hashed)
            )
            user_id = cur.fetchone()[0]
        conn.commit()
    return user_id

def login_user(email, password):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, username, password FROM users WHERE email = %s;", (email,))
            row = cur.fetchone()
            if row and verify_password(password, row[2]):
                return {"id": row[0], "username": row[1]}
    return None
