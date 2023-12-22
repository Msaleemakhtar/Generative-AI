
import streamlit as st


st.line_chart({"data": [1,2,3,4,5,6,7,8,9]})

with st.expander("See the explanation"):
    st.warning("Data is shown")
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're guaranteed to be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg")
    