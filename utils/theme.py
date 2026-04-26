import streamlit as st


def apply_theme():
    st.markdown(
        """
        <style>

        /* page padding */
        .block-container
        {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 1.2rem;
            padding-right: 1.2rem;
            max-width: 700px;
        }

        /* metric cards */
        [data-testid="stMetric"]
        {
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #ECECEC;
        }

        /* form card */
        div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stForm"])
        {
            background-color: white;
            border-radius: 14px;
            padding: 18px;
            border: 1px solid #ECECEC;
        }

        /* buttons */
        .stButton > button
        {
            border-radius: 10px;
            height: 45px;
            font-weight: 600;
        }

        /* input fields */
        input, textarea
        {
            border-radius: 8px !important;
        }

        /* mobile spacing */
        @media (max-width: 640px)
        {
            .block-container
            {
                padding-top: 1rem;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
