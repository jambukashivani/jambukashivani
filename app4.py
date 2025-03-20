import streamlit as st

# Create a narrow column for alignment
col1, _ = st.columns([1, 4])  # 1: Left, 4: Empty space for alignment

with col1:  # Place all elements inside the narrow left column
    for i in range(1, 4): 
        if st.button(f"Input {i}"): 
            st.session_state[f"show_input_{i}"] = True
        if st.session_state.get(f"show_input_{i}", False): 
            st.text_input(f"Enter value {i}", key=f"input_{i}")
