import streamlit as st

st.file_uploader(

    label="Upload PDF below",
    type=["pdf"],
    accept_multiple_files=True

    )