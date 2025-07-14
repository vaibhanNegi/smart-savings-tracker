# pages/_Login.py

import streamlit as st
import pandas as pd
from sqlalchemy import text
from database import engine

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM auth_users WHERE email = :email AND password = :password"),
            {"email": email, "password": password}
        ).fetchone()

    if result:
        st.session_state.logged_in = True
        st.session_state.user = dict(result._mapping)
        st.success(f"Welcome, {st.session_state.user['name']}!")
    else:
        st.error("Invalid email or password.")
