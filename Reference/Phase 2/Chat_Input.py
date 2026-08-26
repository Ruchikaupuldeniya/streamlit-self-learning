"""
Docstring for Phase 2.Streamlit_Input
"""
import streamlit as st

st.text_input(

    label="Password",
    placeholder="Enter your password",
    max_chars=12,
    help="Password must contain 12 charecters",
    type="password"
)

st.text_area(

    label="Feedback form",
    placeholder="Enter your feedback here",
    label_visibility="hidden",
    height=300,
    help="Here you have to five the feedback"
    
)

st.chat_input(

    placeholder="Ask anything...",
    disabled=False
)