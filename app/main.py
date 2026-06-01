

import streamlit as st
import sys
import os



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from db import repositry
from db.database import init_db
from core.expenses import ExpenseManager
from db.repositry import InsertExpenses
from core.managedata import DataManagment

init_db()
expense = ExpenseManager()
expense_service = InsertExpenses()
datamanagment = DataManagment()


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

            expense_service.insert_expense(

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
    with st.container(border=True):
        st.info("📌 Showing the latest 10 expense transactions.")
        data = expense.get_last10_expenses()

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
            df.drop(columns=["id"]),
            use_container_width=True,
            hide_index=True)
                 
    st.divider()
    st.subheader("📋 Expense History By Date")

    start_date = st.date_input("From date")

    end_date = st.date_input("To date")

    if st.button("Show Expenses"):
        st.session_state["filtered_expenses"] = expense.get_expenses_by_date_range(
            start_date,
            end_date,
        )
        st.session_state["selected_start_date"] = start_date
        st.session_state["selected_end_date"] = end_date

    if "filtered_expenses" in st.session_state:

        df = pd.DataFrame(

            st.session_state["filtered_expenses"],

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

        with st.container(border=True):

            st.info(
                f"📌 Showing expenses from "
                f"{st.session_state['selected_start_date']} "
                f"to {st.session_state['selected_end_date']}"
            )

            st.dataframe(

                df.drop(columns=["id"]),

                use_container_width=True,

                hide_index=True

            )

            if st.button("Show Total Summary"):

                totals = expense.get_total_expenses_by_date_range(
                    st.session_state["selected_start_date"],
                    st.session_state["selected_end_date"],
                )

                summary_df = pd.DataFrame(
                    {
                        "category": [
                            "grocery",
                            "dairy",
                            "laundry",
                            "shopping",
                            "fruit_vegetable",
                            "other_bills",
                        ],
                        "total_amount": [
                            value if value is not None else 0 for value in totals
                        ],
                    }
                )

                st.dataframe(
                    summary_df,
                    use_container_width=True,
                    hide_index=True,
                )

with tab3:

    st.subheader("⚙️ Manage Data")

    st.info(

        "Use this section to export, backup, or delete your expense records."

    )

    st.subheader("📤 Export All Expenses")
    st.divider()

    data = datamanagment.get_all_expenses_for_export()
    
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

    csv = df.drop(columns=["id"]).to_csv(index=False).encode("utf-8")

    st.download_button(

        "Download All Expenses",

        data=csv,

        file_name="all_expenses.csv",

        mime="text/csv"

    )

    st.subheader("📅 Export Expenses By Date Range")
    st.divider()

    export_start_date = st.date_input("From date", key="export_start_date")
    export_end_date = st.date_input("To date", key="export_end_date")

    if st.button("Generate Filtered CSV"):
        filtered_data = expense.get_expenses_by_date_range(
            export_start_date,
            export_end_date,
        )

        filtered_df = pd.DataFrame(
            filtered_data,
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

        filtered_csv = filtered_df.drop(columns=["id"]).to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download Filtered Expenses",
            data=filtered_csv,
            file_name=(
                f"expenses_{export_start_date}_to_{export_end_date}.csv"
            ),
            mime="text/csv"
        )

    st.subheader("🗑️ Delete Expenses By Date Range")
    st.divider()

    delete_start_date = st.date_input("Delete from date", key="delete_start_date")
    delete_end_date = st.date_input("Delete to date", key="delete_end_date")

    if st.button("Delete Expenses"):
        st.session_state["pending_delete_confirmation"] = True
        st.session_state["pending_delete_start_date"] = delete_start_date
        st.session_state["pending_delete_end_date"] = delete_end_date

    if st.session_state.get("pending_delete_confirmation"):
        st.warning(
            "All expenses within the selected date range will be permanently removed."
        )

        if st.button("Confirm Delete"):
            datamanagment.delete_expenses_by_date_range(
                st.session_state["pending_delete_start_date"],
                st.session_state["pending_delete_end_date"],
            )
            st.session_state["pending_delete_confirmation"] = False
            st.success("Expenses deleted successfully from selected date range.")

    st.subheader("⚠️ Delete All Expenses")
    st.divider()

    if st.button("Delete All Expenses"):
        st.session_state["pending_delete_all_confirmation"] = True

    if st.session_state.get("pending_delete_all_confirmation"):
        st.warning("All expense records will be permanently deleted.")

        if st.button("Confirm Delete All"):
            datamanagment.delete_all_expenses()
            st.session_state["pending_delete_all_confirmation"] = False
            st.success("All expenses deleted successfully.")
        
