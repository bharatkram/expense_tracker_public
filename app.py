import streamlit as st

from api.total_spend_api import get_this_and_prev_months_total_spend

st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="centered")

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🏠 Expense Tracker")
st.caption("Track and understand your spending")

st.divider()

# ---------------------------------------------------
# SUMMARY CARDS
# ---------------------------------------------------

try:
    data = {}
    with st.spinner("Fetching expense summary..."):
        data = get_this_and_prev_months_total_spend()
except Exception as e:
    st.error(str(e))


this_month_total = 0
last_month_total = 0

if data:
    this_month_total = data["current_month"]["total"]
    last_month_total = data["previous_month"]["total"]

col1, col2 = st.columns(2)

with col1:
    st.metric(label="📅 This Month", value=f"₹{this_month_total}")

with col2:
    st.metric(label="💸 Last Month's Spend", value=f"₹{last_month_total}")

st.write("")

# ---------------------------------------------------
# RECENT EXPENSES
# ---------------------------------------------------

st.subheader("🧾 Recent Expenses")

recent_expenses = [
    {"date": "2026-03-08", "category": "Food", "amount": 250},
    {"date": "2026-03-07", "category": "Groceries", "amount": 800},
    {"date": "2026-03-06", "category": "Transport", "amount": 120},
]

st.table(recent_expenses)

st.divider()

# ---------------------------------------------------
# NAVIGATION BUTTONS
# ---------------------------------------------------

col1, col2 = st.columns(2, gap="xxsmall")

with col1:
    if st.button("➕ Add Expense", width="content", type="primary"):
        st.switch_page("pages/add_expense.py")

with col2:
    if st.button("📜 History", width="content", type="primary"):
        st.switch_page("pages/history.py")
