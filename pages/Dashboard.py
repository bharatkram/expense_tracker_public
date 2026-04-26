import streamlit as st
import pandas as pd
import calendar

st.title("📊 Expense Dashboard")
st.caption("Overview of your spending")

st.divider()

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------


@st.cache_data
def load_data():
    df = pd.read_csv("data/results.csv")
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    df["month_name"] = df["month"].apply(lambda x: calendar.month_abbr[int(x)])
    return df


df = load_data()

# ---------------------------------------------------
# FILTERS
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    year_filter = st.selectbox("Year", ["All"] + sorted(df["year"].unique().tolist()))

with col2:
    user_filter = st.selectbox("User", ["All"] + sorted(df["user"].unique().tolist()))

filtered_df = df.copy()

if year_filter != "All":
    filtered_df = filtered_df[filtered_df["year"] == year_filter]

if user_filter != "All":
    filtered_df = filtered_df[filtered_df["user"] == user_filter]

st.divider()

# ---------------------------------------------------
# METRICS
# ---------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Spent", f"₹{filtered_df['cost'].sum():,.0f}")

with col2:
    st.metric("Transactions", len(filtered_df))

with col3:
    st.metric("Avg Expense", f"₹{filtered_df['cost'].mean():,.0f}")

st.divider()

# ---------------------------------------------------
# MONTHLY TREND
# ---------------------------------------------------

st.subheader("📈 Monthly Spending Trend")

monthly = filtered_df.groupby("month_name")["cost"].sum()

month_order = list(calendar.month_abbr)[1:]

monthly = monthly.reindex(month_order)

st.line_chart(monthly)

st.divider()

# ---------------------------------------------------
# CATEGORY + USER CHARTS
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📂 Spending by Category")

    category_spend = (
        filtered_df.groupby("item")["cost"].sum().sort_values(ascending=False)
    )

    st.bar_chart(category_spend)

with col2:

    st.subheader("👤 Spending by User")

    user_spend = filtered_df.groupby("user")["cost"].sum()

    st.bar_chart(user_spend)

st.divider()

# ---------------------------------------------------
# RECENT EXPENSES
# ---------------------------------------------------

st.subheader("🧾 Recent Expenses")

recent = filtered_df.sort_values("date", ascending=False).head(5)

display_df = recent[["date", "item", "cost", "placeOfPurchase", "user"]].rename(
    columns={
        "date": "Date",
        "item": "Category",
        "cost": "Amount",
        "placeOfPurchase": "Place",
        "user": "User",
    }
)

st.dataframe(display_df, width="stretch")
