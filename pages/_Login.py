# pages/_Login.py

import streamlit as st

def main():
    st.title("🔐 User Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("Logged in successfully")
            # Baad me session/state add karenge
        else:
            st.error("Invalid credentials")

if __name__ == "__main__":
    main()
