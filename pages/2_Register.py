import streamlit as st
from db import insert_user, create_user_table
import psycopg2

st.title("📝 Register")
create_user_table()  # ensure table exists

# form inputs
name    = st.text_input("Name")
email   = st.text_input("Email")
password= st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    if password != confirm:
        st.error("Passwords do not match.")
    elif not name or not email or not password:
        st.warning("Fill all fields.")
    else:
        try:
            insert_user(name, email, password)
            st.success("✅ Registered successfully! Now login.")
        except psycopg2.errors.UniqueViolation:
            st.error("❌ Email already registered.")
        except Exception as e:
            st.error(f"Error: {e}")
