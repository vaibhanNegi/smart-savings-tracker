import streamlit as st
from auth import login_user

st.title("🔐 Login")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = login_user(email.strip(), password)
    if user:
        st.session_state.logged_in = True
        st.session_state.user_id = user["id"]
        st.session_state.username = user["username"]
        st.success(f"Welcome, {user['username']}!")
    else:
        st.error("Invalid credentials.")
