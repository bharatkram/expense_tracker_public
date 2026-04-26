from datetime import date
import re

import streamlit as st

from utils.fixed_lists import categories, users


def initialize_form_state():
    defaults = {
        "expense_date": date.today(),
        "user": users[0],
        "category": None,
        "seller": "",
        "amount": 0.0,
        "description": "",
    }

    # Reset form when requested
    if st.session_state.get("reset_form", False):
        for k, v in defaults.items():
            st.session_state[k] = v
        st.session_state.reset_form = False

    # Initialize missing keys
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def render_expense_form():

    initialize_form_state()

    with st.container(border=True):

        st.subheader("🧾 Expense Details")

        expense_date = st.date_input(
            "📅 Date",
            key="expense_date",
        )

        user = st.segmented_control(
            "User",
            options=users,
            key="user",
        )

        category = st.selectbox(
            "📂 Category",
            categories,
            key="category",
            placeholder="Select category...",
        )

        seller = st.text_input(
            "🏪 Merchant / Seller",
            key="seller",
            placeholder="Example: Amazon, Uber, Starbucks",
        )

        amount = st.number_input(
            "💰 Amount",
            key="amount",
            min_value=0.0,
            format="%.2f",
        )

        description = st.text_area(
            "📝 Description (optional)",
            key="description",
            placeholder="Add notes about the purchase",
        )

        submit = st.button("➕ Add Expense", width="stretch")

    if not submit:
        return None

    expense_data = {
        "date": expense_date.isoformat(),
        "user": re.sub(r"[^A-Za-z0-9 ]+", "", user).strip().lower(),
        "category": (
            re.sub(r"[^A-Za-z0-9 &]+", "", category).strip().lower() if category else ""
        ),
        "seller": seller.strip().lower(),
        "amount": amount,
        "description": description.strip().lower(),
    }

    return expense_data
