import streamlit as st

st.selectbox(
    label="Select below",
    placeholder="Select the options",
    options=["A", "B", "C"],
    help="Select from the options",
    label_visibility="visible",
    index=None,
)
st.multiselect(
    label="Select below",
    options=["A", "B", "C", "D"],
    help="select the options",
    label_visibility="visible",) 

st.radio(
        label="Select the options below",
        options=["A", "B", "C", "D"],
        label_visibility="visible",
        help="Select from the options",
        index=None
)
st.checkbox(
    "Accept Terms & Conditions",
    value=False
)