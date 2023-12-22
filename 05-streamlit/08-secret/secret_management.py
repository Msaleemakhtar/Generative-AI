import streamlit as st


st.write("DB username is : ", st.secrets.get("db_username"))
st.write("DB password is : ", st.secrets.get("db_password"))




import os

os.environ["db_username"] == st.secrets.get("db_username")


st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)