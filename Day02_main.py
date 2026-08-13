import streamlit as st


st.markdown("# Hi , i am Ruchika")
st.markdown("## I am a Data Scientist and Machine Learning Engineer")
st.markdown("### I have 2 years of **experience in Data Science** and Machine Learning")



st.markdown(">  Hi , i am Ruchika")
st.markdown("1. Hi\n , i am Ruchika")

str = "print('Hello World')"
st.code(str) 
st.markdown("---")
st.markdown("[Google](https://www.google.com/")

table = '''
| Name | Age | City |
|------|-----|------|   
| John | 25  | New York |
| Jane | 30  | London |     
| Mike | 35  | Paris |
'''     
st.markdown(table)

json = {"name": "John", "age": 30, "city": "New York"   }
st.json(json)   

st.markdown('that is so funny ! : joy :')  