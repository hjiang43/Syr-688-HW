import streamlit as st

def run_requirements_page():
    st.title("Requirements Page")

    if st.button("Get requirement libraries and modules list"):
        st.write("Here is the project requirements information.")
