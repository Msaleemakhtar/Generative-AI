import streamlit as st
import time

with st.status("Downloading.......", expanded=True) as status:
    st.write("loading......")
    time.sleep(2)
    st.write("searching Url...........")
    time.sleep(1)
    st.write("Downloading data ........")
    time.sleep(1)
    status.update(label="Download Complted!",state="complete", expanded=False)
st.button("Rerun")


