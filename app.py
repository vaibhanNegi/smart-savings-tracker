import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Smart Savings App",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("💼 Welcome to SmartSavings App")
st.markdown("""
Use the sidebar to navigate between:
- 📊 SmartSavings Predictor
- 🧠 Expense Category Analyzer
- 📈 Monthly Trend
- 💸 Budget Recommender
""")
