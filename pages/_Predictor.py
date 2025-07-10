import streamlit as st
import pandas as pd
import os
from datetime import date

st.title("📊 SmartSavings Predictor")

# Monthly Income Input
st.sidebar.header("💰 Monthly Income")
monthly_income = st.sidebar.number_input("Enter Monthly Income (₹)", min_value=0, value=30000, step=500)

st.markdown("### 🧾 Log Your Expense")
with st.form("expense_form"):
    col1, col2 = st.columns(2)

    with col1:
        amount = st.number_input("Amount Spent (₹)", min_value=0, value=1000, step=100)
        category = st.selectbox("Spending Category", ["Grocery", "Rent", "Entertainment", "Health", "EMI"])
        transaction = st.selectbox("Transaction Type", ["Essential", "Non-Essential"])
    
    with col2:
        method = st.selectbox("Payment Method", ["Cash", "Card", "Online"])
        date_input = st.date_input("Date of Expense", value=date.today())
    
    submitted = st.form_submit_button("➕ Add Expense")

# Handle Form Submission
if submitted:
    # Extract components from date
    day = date_input.day
    month_num = date_input.month
    weekday = date_input.strftime("%A")

    # Create row
    new_row = pd.DataFrame([{
        "Amount": amount,
        "Income": monthly_income,
        "month_num": month_num,
        "Day": day,
        "Type": transaction,
        "Payment_Method": method,
        "Category": category,
        "Weekday": weekday,
        "Savings": monthly_income  # Temporary, will calculate below
    }])

    try:
        # Append to CSV
        if os.path.exists("user_data.csv"):
            existing = pd.read_csv("user_data.csv")
            full = pd.concat([existing, new_row], ignore_index=True)
        else:
            full = new_row

        # 🧮 Calculate total expense and new savings
        total_expense = full["Amount"].sum()
        new_saving = monthly_income - total_expense
        full["Savings"] = new_saving

        # Keep last 5 entries
        full = full.tail(5)
        full.to_csv("user_data.csv", index=False)

        st.success(f"✅ Expense added! New Estimated Savings: ₹{new_saving:,.2f}")
    except PermissionError:
        st.error("Permission Denied: Close the 'user_data.csv' file before submitting.")
    except Exception as e:
        st.error(f"Error while saving: {e}")
