# pages/_Register.py

import streamlit as st
from database import engine
import pandas as pd
from sqlalchemy import text

st.title("🔐 User Registration")

with st.form("register_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Register")

    if submit:
        if name and email and password:
            with engine.connect() as conn:
                query = text("""
                    INSERT INTO auth_users (name, age, email, password)
                    VALUES (:name, :age, :email, :password)
                """)
                conn.execute(query, {"name": name, "age": age, "email": email, "password": password})
                conn.commit()
                st.success("Registration successful! Please log in.")
        else:
            st.warning("Please fill all required fields.")
