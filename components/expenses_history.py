from datetime import date
import re

import pandas as pd
import streamlit as st

from utils.fixed_lists import categories, users


def get_empty_list_for_display_df():
    return [
        {
            "date": "",
            "user": "",
            "category": "",
            "amount": 0,
            "seller": "",
            "description": "",
        }
    ]


def initialize_form_state():
    defaults = {
        "expense_date": date.today(),
        "user": users[0],
        "category": None,
        "seller": "",
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

    if "show_filters" not in st.session_state:
        st.session_state.show_filters = True

    if "transactions_count" not in st.session_state:
        st.session_state.transactions_count = 0

    if "filtered_df" not in st.session_state:
        st.session_state.filtered_df = pd.DataFrame(get_empty_list_for_display_df())


def render_history_filters():
    st.subheader("Filters")

    date_filter = st.date_input("📅 Date", key="filter_date")

    category_filter = st.selectbox(
        "📂 Category", ["All"] + categories, key="filter_category"
    )

    user_filter = st.selectbox("User", ["All"] + users, key="filter_user")

    seller_filter = st.text_input("🏪 Merchant / Seller", key="filter_seller")

    if st.button("Apply Filters"):

        applied_filters = {}

        if date_filter:
            applied_filters["date"] = date_filter.isoformat()

        if category_filter != "All":
            applied_filters["category"] = (
                re.sub(r"[^A-Za-z0-9 &]+", "", category_filter).strip().lower()
            )

        if user_filter != "All":
            applied_filters["user"] = (
                re.sub(r"[^A-Za-z0-9 ]+", "", user_filter).strip().lower()
            )

        if seller_filter:
            applied_filters["seller"] = seller_filter

        return applied_filters


def render_history_table():

    if st.button("🔍 Modify Filters"):
        st.session_state.show_filters = True
        st.rerun()

    filtered_df = st.session_state.filtered_df

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Transactions", st.session_state.transactions_count)

    with col2:
        st.metric("Total", f"₹{filtered_df['amount'].sum():,.0f}")

    st.divider()

    display_df = filtered_df[
        ["date", "category", "amount", "seller", "user", "description"]
    ].rename(
        columns={
            "date": "Date",
            "category": "Category",
            "amount": "Amount",
            "seller": "Seller",
            "user": "User",
            "description": "Description",
        }
    )

    st.dataframe(display_df, width="stretch")
