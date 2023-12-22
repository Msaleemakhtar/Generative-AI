import streamlit as st

st.header("Counter With Session State")

st.write(st.session_state)

if "count" not in st.session_state:
    st.session_state.count = 0

increament = st.button("Increment")

if increament:
    st.session_state.count+=1

st.write("counter state : ", st.session_state.count)

# del st.session_state.count

#"Text" , st.session_state.count

