import streamlit as st


col1, col2, col3 = st.columns([1, 4, 4], gap=("large"))
with col1:
    st.image("https://d3nn873nee648n.cloudfront.net/900x600/20669/300-SM1067010.jpg")

with col2:
    st.image("https://d3nn873nee648n.cloudfront.net/900x600/20669/300-SM1067010.jpg")


with col3:
    st.image("https://d3nn873nee648n.cloudfront.net/900x600/20669/300-SM1067010.jpg")

st.write("------------------------------------------------------------------------------")

col1, col2, col3 = st.columns([1, 4, 4], gap=("large"))
col1.image("https://d3nn873nee648n.cloudfront.net/900x600/20669/300-SM1067010.jpg")

col2.image("https://d3nn873nee648n.cloudfront.net/900x600/20669/300-SM1067010.jpg")


col3.image("https://d3nn873nee648n.cloudfront.net/900x600/20669/300-SM1067010.jpg")