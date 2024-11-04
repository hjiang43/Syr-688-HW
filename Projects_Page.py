import streamlit as st

def run_projects_page():
    st.title("Projects Assistance")

    # Add the text between the title and the chat section
    st.write("Project vectorDB is creating...")

    # Horizontal line to separate the text from the chat section
    st.markdown("---")  # A horizontal line separator

    # Chat Input at the bottom
    st.subheader("Chat with the Bot")

    chat_input = st.text_input("Enter your message here:")

    if chat_input:
        # Simulate chat response
        st.write(f"**You:** {chat_input}")
        st.write("**Bot:** This is a placeholder response for the chat message.")
