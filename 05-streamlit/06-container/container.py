
import streamlit as st
import numpy as np

with st.container():
    st.write("This is inside the container")

    st.area_chart(np.random.randn(50, 4))
    st.camera_input("Take a picture")