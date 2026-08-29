import streamlit as st

import pandas as pd

# Title
st.title("Streamlit Elements Demo")

# Dataframe Section
st.subheader("Dataframe")

df = pd.DataFrame({
    
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    
    'Age': [25, 32, 37, 45],
    
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Chef']
    
})
st.dataframe(df)

# Data Editor Section (Editable Dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df)

print(editable_df)

# Static Table Section
st.subheader("Static Table")

st.table(df)

# Metrics section
st.subheader("Metrics")
st.metric(label = 'Total Rows', value = len(df))

st.metric(label = 'Average Age', value = round(df['Age'].mean(), 1))

# JSON and DICT Section
st.subheader("JSON and DICTIONARY")

sample_dict = {
    
    'Name': 'Alice',
    
    'Age': 25,
    
    'Skills': ['Python', 'Data Science', 'Machine Learning']
    
}
st.json(sample_dict)

# Also Show It As Dictionary
st.write("Dictionary View:", sample_dict)