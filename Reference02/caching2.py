import streamlit as st

file_path = "example.txt"

@st.cache_resource

def get_file_handler():

    # Open the file in append mode, which creates the file if it doesn't exist
    file = open(file_path, "a+")

    return file

# Use the cached file handler
file_handler = get_file_handler()

# Write to the file using the cached handler
if st.button("Write to file"):
    
    file_handler.write("New line of text\n")
    
    file_handler.flush()  # Ensure data is written immediately
    
    st.success("Wrote a new line to the file!")

# Read and display the file contents
if st.button("Read File"):
    
    file_handler.seek(0)  # Move to the start of the file
    
    content = file_handler.read()
    
    st.text(content)

# Close the file handler when the app stops
st.button("Close File", on_click = file_handler.close)