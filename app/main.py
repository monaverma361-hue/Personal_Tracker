import streamlit as st
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from db.database import init_db
from db.repositry import ExpenseRepository

init_db()
expense = ExpenseRepository()


st.set_page_config(
    page_title="PersonalTracker",
    page_icon= "🚀",
    layout="wide"
)
st.title("📊Personal Expense Manager")
st.divider()

tab1, tab2, tab3 = st.tabs([

    "➕ Add Expense",

    "📋 View Expenses",

    "🛠️ Manage Data"

])

with tab1:
    st.subheader("💰 Add Expenses")

    with st.form("expense_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:

            grocery = st.number_input("Grocery", min_value=0.0, step=1.0)

            dairy = st.number_input("Dairy", min_value=0.0, step=1.0)

            laundry = st.number_input("Laundry", min_value=0.0, step=1.0) 

            payment_mode = st.text_input("Enter payment method")

        with col2:

            shopping = st.number_input("Shopping", min_value=0.0, step=1.0)

            fruit_vegetable = st.number_input("Fruit and Vegetable", min_value=0.0, step=1.0)

            other_bills = st.number_input("Other Bills", min_value=0.0, step=1.0)

            date = st.date_input("Date")

        submitted = st.form_submit_button("Enter")

        if submitted:

            expense.insert_expense(

                grocery,

                dairy,

                laundry,

                payment_mode,

                shopping,

                fruit_vegetable,

                other_bills,

                date,

            )

            st.success("Expense saved successfully.")

        

    
with tab2:
    st.subheader("📋 Expense History")
    st.info("📌 Showing the latest 10 expense transactions.")
    data = expense.get_all_expenses()

    import pandas as pd

    df = pd.DataFrame(

    data,

    columns=[
    "id",
    "grocery",
    "dairy",
    "laundry",
    "payment_mode",
    "shopping",
    "fruit_vegetable",
    "other_bills",
    "date"
]

)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True)
                 
                 

