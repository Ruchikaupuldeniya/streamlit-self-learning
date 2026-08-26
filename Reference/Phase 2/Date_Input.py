import streamlit as st
import datetime

st.date_input(
    "Select date of birth",
    value=None,
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date.today(),
    help="Select your correct date of birth"
)

st.time_input(
    label="Enter time",
    value=datetime.datetime.now().time()
)


date = st.date_input(

    label="Enter date",
    value=None
)

time = st.time_input(

    label="Enter time",
    value=None
)

if date and time:

    dt = datetime.datetime.combine(date, time)
    st.write(dt)