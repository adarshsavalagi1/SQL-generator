import streamlit as st
from utils.prompts import create_sql_prompt_template
from utils.engine import chat

def generate_sql_query(prompt):
    return chat(create_sql_prompt_template(prompt))


st.title("SQL Query Generator")


user_prompt = st.text_area("Enter your prompt here:", height=150)


if st.button("Generate SQL Query"):
    if user_prompt:
        sql_query = generate_sql_query(user_prompt)
        st.markdown(sql_query)  
    else:
        st.error("Please enter a prompt.")
