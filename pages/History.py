import streamlit as st

import pandas as pd

from components.expenses_history import (
    get_empty_list_for_display_df,
    initialize_form_state,
    render_history_filters,
    render_history_table,
)
from services.expense_service import get_expenses

initialize_form_state()

st.set_page_config(
    page_title="Add Expense",
    page_icon="💳",
    layout="centered",
)

st.title("💳 Add Expense")
st.caption("Track your daily spending")

st.divider()


# ---------------------------------------------------
# ERROR PLACEHOLDER
# ---------------------------------------------------

error_placeholder = st.empty()


# ---------------------------------------------------
# SHOW FILTERS OR FILTERED DATA
# ---------------------------------------------------

expense_data = None

if st.session_state.get("show_filters"):
    expense_data = render_history_filters()
else:
    render_history_table()


# ---------------------------------------------------
# FILTERS QUERY
# ---------------------------------------------------

if expense_data:

    success, result = get_expenses(expense_data)

    if success:

        st.session_state.transactions_count = result.get("count")
        st.session_state.filtered_df = pd.DataFrame(
            result.get("expenses") or get_empty_list_for_display_df()
        )
        st.session_state.show_filters = False
        st.rerun()

    else:

        error_placeholder.error(f"API Error: {result}")
