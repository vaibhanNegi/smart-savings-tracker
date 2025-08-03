import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # loads .env in local dev; on Streamlit Cloud env is already injected
DATABASE_URL = os.getenv("DB_URL")
if not DATABASE_URL:
    raise RuntimeError("DB_URL missing. Set it in .env or Streamlit secrets.")

def get_conn():
    return psycopg2.connect(DATABASE_URL, sslmode="require")  # Supabase needs sslmode=require

def create_tables():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_profiles (
                    user_id INT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
                    age INT,
                    monthly_income FLOAT,
                    savings_amount FLOAT,
                    spending_amount FLOAT,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
        conn.commit()
