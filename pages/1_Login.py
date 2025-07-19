import streamlit as st
from db import login_user

st.title("🔐 Login")
username = st.text_input("Username")
email    = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = login_user(username, email, password)
    if user:
        st.session_state["logged_in"] = True
        st.session_state["user_id"]   = user[0]
        st.session_state["username"]  = user[1]
        st.success(f"Welcome, {user[1]}!")
        
    else:
        st.error("❌ Invalid email or password.")
