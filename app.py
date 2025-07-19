
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns


# app.py



# Stop access if not logged in
if not st.session_state.get("logged_in"):
    st.warning("Please login to access the dashboard.")
    st.stop()

# Dashboard title
st.title("🎯 Smart Saving Dashboard")

# Show welcome message using username
st.success(f"Welcome, {st.session_state.get('username', 'User')}!")








