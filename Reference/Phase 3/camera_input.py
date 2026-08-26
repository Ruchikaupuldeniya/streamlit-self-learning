import streamlit as st

image = st.camera_input(
    "capture image"
)

if image:

    st.image(image=image)