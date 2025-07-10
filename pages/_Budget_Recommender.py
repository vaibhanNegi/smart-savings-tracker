
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💡 Budget Recommender Based on Your Income")

income = st.number_input("Enter Monthly Income (₹)", min_value=0, step=1000)

if income > 0:
    allocation = {
        "Grocery": income * 0.25,
        "Rent": income * 0.20,
        "EMI": income * 0.15,
        "Health": income * 0.10,
        "Entertainment": income * 0.10,
        "Savings": income * 0.20
    }

    df = pd.DataFrame(list(allocation.items()), columns=["Category", "Recommended Amount (₹)"])
    st.dataframe(df, use_container_width=True)

    fig, ax = plt.subplots()
    ax.pie(df["Recommended Amount (₹)"], labels=df["Category"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💡 Budget Recommender Based on Your Income")

income = st.number_input("Enter Monthly Income (₹)", min_value=0, step=1000)

if income > 0:
    allocation = {
        "Grocery": income * 0.25,
        "Rent": income * 0.20,
        "EMI": income * 0.15,
        "Health": income * 0.10,
        "Entertainment": income * 0.10,
        "Savings": income * 0.20
    }

    df = pd.DataFrame(list(allocation.items()), columns=["Category", "Recommended Amount (₹)"])
    st.dataframe(df, use_container_width=True)

    fig, ax = plt.subplots()
    ax.pie(df["Recommended Amount (₹)"], labels=df["Category"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

