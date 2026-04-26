import streamlit as st

from components.expense_form import render_expense_form
from validators.expense_validator import validate_expense
from services.expense_service import save_expense


st.set_page_config(
    page_title="Add Expense",
    page_icon="💳",
    layout="centered",
)

st.title("💳 Add Expense")
st.caption("Track your daily spending")

st.divider()


# ---------------------------------------------------
# SUCCESS MODAL
# ---------------------------------------------------


@st.dialog("Expense Added")
def success_modal():

    st.success("✅ Expense added successfully!")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Add Another"):
            st.session_state.reset_form = True
            st.rerun()

    with col2:
        if st.button("🏠 Go Home"):
            st.switch_page("app.py")


# ---------------------------------------------------
# ERROR PLACEHOLDER
# ---------------------------------------------------

error_placeholder = st.empty()


# ---------------------------------------------------
# FORM
# ---------------------------------------------------

expense_data = render_expense_form()


# ---------------------------------------------------
# FORM SUBMISSION
# ---------------------------------------------------

if expense_data:

    errors = validate_expense(expense_data)

    if errors:

        error_placeholder.error(
            "Please fix the following issues:\n\n" + "\n".join(f"• {e}" for e in errors)
        )

    else:

        success, result = save_expense(expense_data)

        if success:

            st.session_state.show_success_modal = True
            st.session_state.reset_form = True
            st.rerun()

        else:

            error_placeholder.error(f"API Error: {result}")


# ---------------------------------------------------
# TRIGGER SUCCESS MODAL
# ---------------------------------------------------

if st.session_state.get("show_success_modal"):

    st.session_state.show_success_modal = False
    success_modal()
