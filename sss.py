import pandas as pd
import streamlit as st
# Dummy Prediction Function
def predict(values):
    return np.sum(values)  # Example: Summing input values as a simple "prediction"

# Initialize session state for input visibility
if "show_inputs" not in st.session_state:
    st.session_state.show_inputs = False

# Show inputs when button is clicked
if st.button("Enter Inputs"):
    st.session_state.show_inputs = True

# Take inputs if button was clicked
if st.session_state.show_inputs:
    input1 = st.number_input("Enter first value:", key="input1")
    input2 = st.number_input("Enter second value:", key="input2")
    input3 = st.number_input("Enter third value:", key="input3")

    # Predict button
    if st.button("Predict"):
        values = [input1, input2, input3]  # Collect inputs
        prediction = predict(values)  # Pass to the model
        st.success(f"Prediction Result: {prediction}")
