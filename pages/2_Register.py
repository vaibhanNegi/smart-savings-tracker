import streamlit as st
from db import create_tables
from auth import register_user

create_tables()

st.title("📝 Register")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    if not username or not email or not password:
        st.error("Fill all fields.")
    elif password != confirm:
        st.error("Passwords do not match.")
    else:
        try:
            register_user(username.strip(), email.strip(), password)
            st.success("Registered successfully! Now login.")
        except Exception as e:
            if "duplicate key" in str(e).lower():
                st.error("Username or email already exists.")
            else:
                st.error(f"Error: {e}")
