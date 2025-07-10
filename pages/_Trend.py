import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import os

st.title("📈 Monthly Savings Trend")

if not os.path.exists("user_data.csv"):
    st.warning("No data available.")
else:
    df = pd.read_csv("user_data.csv")

    if df.empty or "month_num" not in df.columns or "Savings" not in df.columns:
        st.warning("No valid data to display trend.")
    else:
        df["month_num"] = pd.to_numeric(df["month_num"], errors="coerce")
        df = df.dropna(subset=["month_num", "Savings"])
        df["month_num"] = df["month_num"].astype(int)

        trend = df.groupby("month_num")["Savings"].mean().reset_index()

        if trend.empty:
            st.warning("Not enough data to generate trend chart.")
        else:
            trend["Month"] = trend["month_num"].apply(lambda x: calendar.month_name[x])
            fig, ax = plt.subplots()
            ax.plot(trend["month_num"], trend["Savings"], marker='o', color='royalblue')
            ax.set_xticks(trend["month_num"])
            ax.set_xticklabels(trend["Month"], rotation=45)
            ax.set_title("Average Savings by Month")
            ax.set_xlabel("Month")
            ax.set_ylabel("Savings (₹)")
            ax.grid(True)
            st.pyplot(fig)
