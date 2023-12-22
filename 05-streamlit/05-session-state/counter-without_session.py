import streamlit as st

''' 
Counter without Session State
No matter how many times we press the Increment button in 
the above app, the count remains at 1. Let's understand why:

Each time we press the Increment button, Streamlit reruns 
counter_without_session.py from top to bottom, and with every run, count 
gets initialized to 0 .

Pressing Increment subsequently adds 1 to 0, thus count=1
no matter how many times we press Increment.

'''

st.header("Counter Without Session State")

count= 0

increament = st.button("Increment")
if increament:
    count +=1

st.write("counter : ", count)