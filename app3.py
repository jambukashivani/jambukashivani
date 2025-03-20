import streamlit as st

for i in range(1, 4): 
    if st.button(f"Input {i}"): st.session_state[f"show_input_{i}"] = True
    if st.session_state.get(f"show_input_{i}", False): st.text_input(f"Enter value {i}", key=f"input_{i}")
