
import streamlit as st
import numpy as np
import time
with st.empty():
    for seconds in range(10):
        st.write(f"⏳{seconds} are running")
        time.sleep(2)
        st.write("✔️ 10 seconds over!")

st.write("✔️ otside the block")
