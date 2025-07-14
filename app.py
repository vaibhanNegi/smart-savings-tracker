
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns



st.title("💼 Welcome to SmartSavings App")
st.markdown("""
Use the sidebar to navigate between:
- 📊 SmartSavings Predictor
- 🧠 Expense Category Analyzer
- 📈 Monthly Trend
- 💸 Budget Recommender
""")

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
