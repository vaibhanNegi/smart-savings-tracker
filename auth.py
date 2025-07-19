
from db import engine
from sqlalchemy import text
import bcrypt

def register_user(name, age, email, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    with engine.connect() as conn:
        query = text("""
            INSERT INTO auth_users (name, age, email, password)
            VALUES (:name, :age, :email, :password)
        """)
        conn.execute(query, {"name": name, "age": age, "email": email, "password": hashed})
        conn.commit()

def validate_user(email, password):
    with engine.connect() as conn:
        query = text("SELECT password FROM auth_users WHERE email = :email")
        result = conn.execute(query, {"email": email}).fetchone()
        if result:
            return bcrypt.checkpw(password.encode(), result[0].encode())
    return False
