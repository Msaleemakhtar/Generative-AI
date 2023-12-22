import streamlit as st


st.header("Counter Callbacks")

st.write(st.session_state)

if "count" not in st.session_state:
    st.session_state.count = 0

input = st.number_input("Enter a Value", value=0, step=1)

def counter_callbacks(input):
    #st.session_state.count +=1
    st.session_state.count +=input
# st.button("Increament", on_click=counter_callbacks)
st.button("Increament", on_click=counter_callbacks, args=(input,))

st.write("Count : ", st.session_state.count)
