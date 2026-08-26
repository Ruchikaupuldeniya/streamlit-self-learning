import streamlit as st

color = st.color_picker(
    "choose colour"
)
if color:

    st.write(color)