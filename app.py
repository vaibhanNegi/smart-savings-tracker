
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns


# app.py


st.set_page_config(page_title="Smart Savings Tracker", layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first to access the dashboard.")
    st.stop()

st.title("📊 Welcome to Smart Savings Dashboard")
st.write(f"👤 Logged in as: {st.session_state.user['name']}")




from sqlalchemy import create_engine
import psycopg2

# PostgreSQL credentials
db_username = 'postgres'
db_password = '1234'
db_host = 'localhost'
db_port = '5432'
db_name = 'smart_saving_db'

# SQLAlchemy connection URL
DATABASE_URL = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
