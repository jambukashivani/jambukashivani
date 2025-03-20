import streamlit as st
st.title("my first")
st.write("hello")

# Initialize session state
if "show_input" not in st.session_state:
    st.session_state.show_input = False

# Function to update session state when button is clicked
def show_text_input():
    st.session_state.show_input = True

# Button to show the input field
st.button("Click to enter input", on_click=show_text_input)

# Display the input field only if the button was clicked
if st.session_state.show_input:
    user_input = st.text_input("Enter something:")
    if user_input:
        st.write("You entered:", user_input)

