
import streamlit as st



# sidebar
add_selectbox = st.sidebar.selectbox(
    "Please select any one of them", 
    ("Email", "phone", "facebook")
)


with st.sidebar:
    pick_one = st.radio(
        "Please select any one of them", 
    ("Email", "phone", "facebook")

    )


with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )




# main

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)