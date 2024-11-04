import streamlit as st

def run_faq_page():
    st.title("FAQ Page")

    if st.button("Get frequently asked questions"):
        st.write("Here is the frequently asked information.")
