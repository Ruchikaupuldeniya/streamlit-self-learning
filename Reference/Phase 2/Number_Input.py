import streamlit as st

st.number_input(

    label="Age",
    min_value=18,
    max_value=100,
    disabled=False,
    help="Age allowed : 18 -> 100",
    step=1,
    icon=None
)

st.slider(

    label="Batch_size",
    min_value=18,
    max_value=100,
    help="Age allowed : 18 - 100",
    step=1
)