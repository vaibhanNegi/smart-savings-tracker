
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("## 📊 Expense Data Analyzer")
st.markdown("---")

try:
    df = pd.read_csv("user_data.csv")

    if df.empty:
        st.warning("CSV is empty. Please add some data.")
    else:
        # Chart 1: Total Spending by Category (Bar Chart)
        st.subheader("1️⃣ Total Spending by Category")
        if "Category" in df.columns and "Amount" in df.columns:
            category_totals = df.groupby("Category")["Amount"].sum().reset_index()
            if not category_totals.empty:
                fig1, ax1 = plt.subplots(figsize=(8, 4))
                sns.barplot(data=category_totals, x="Category", y="Amount", ax=ax1)
                ax1.set_title("Total Spending by Category")
                ax1.set_ylabel("Amount (₹)")
                ax1.set_xlabel("Category")
                st.pyplot(fig1)
            else:
                st.warning("No data to show category-wise bar chart.")

        # Chart 2: Pie Chart of Spending Category Distribution
        st.subheader("2️⃣ Spending Distribution (Pie Chart)")
        if "Amount" in df.columns and "Category" in df.columns and not category_totals.empty:
            fig2, ax2 = plt.subplots()
            ax2.pie(category_totals["Amount"], labels=category_totals["Category"],
                    autopct='%1.1f%%', startangle=140)
            ax2.axis("equal")
            st.pyplot(fig2)

        # Chart 3: Line Chart of Expense Trend by Entry
        st.subheader("3️⃣ Expense Trend (Line Chart)")
        if "Amount" in df.columns:
            df["Entry"] = range(1, len(df) + 1)
            fig3 = plt.figure()
            sns.lineplot(data=df, x="Entry", y="Amount", marker="o")
            plt.title("Recent Expense Trend")
            plt.xlabel("Entry")
            plt.ylabel("Amount Spent (₹)")
            st.pyplot(fig3)

        # Chart 4: Count of Payment Method
        st.subheader("4️⃣ Most Used Payment Method")
        if "Payment_Method" in df.columns:
            fig4 = plt.figure(figsize=(6, 4))
            sns.countplot(data=df, x="Payment_Method", palette="Set2")
            plt.title("Payment Method Usage")
            plt.xlabel("Method")
            plt.ylabel("Count")
            st.pyplot(fig4)

        # Chart 5: Heatmap of Category vs Day
        st.subheader("5️⃣ Heatmap of Category by Day (Bonus)")
        if "Category" in df.columns and "Day" in df.columns:
            df["Day"] = pd.to_numeric(df["Day"], errors="coerce")
            heatmap_data = pd.crosstab(df["Day"], df["Category"])
            if not heatmap_data.empty:
                fig5, ax5 = plt.subplots(figsize=(8, 5))
                sns.heatmap(heatmap_data, annot=True, fmt='d', cmap="Blues", ax=ax5)
                ax5.set_title("Category Frequency by Day")
                st.pyplot(fig5)
            else:
                st.warning("Not enough data to generate heatmap.")
        else:
            st.warning("Columns 'Category' or 'Day' missing for heatmap.")

except FileNotFoundError:
    st.error("user_data.csv not found. Please run the predictor page first.")
except Exception as e:
    st.error(f"Something went wrong: {e}")

