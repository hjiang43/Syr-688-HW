import PyPDF2
import openai
import streamlit as st
from openai import OpenAI

def check_openai_api_key(api_key):
    client = OpenAI(api_key=api_key)
    try:
        client.models.list()
    except openai.AuthenticationError:
        return False
    else:
        return True

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text


# Show title and description.
st.title("MY Document question answering")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")

if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")

else:
    # a. Validate the key as soon as it is entered rather than validating after the question is asked.
    # I save API key into .env file, and check the type in value with my apt key. and .env file keep in my local
    # if openai_api_key == os.getenv('OPENAI_API_KEY') or check_openai_api_key(openai_api_key):
    if check_openai_api_key(openai_api_key):
        st.success("Valid OpenAI API key")

        # Create an OpenAI client.
        client = OpenAI(api_key=openai_api_key)

        if "question" not in st.session_state:
            st.session_state.question = ""

        # Let the user upload a file via `st.file_uploader`.
        uploaded_file = st.file_uploader(
            "Upload a document (.txt or .pdf)", type=("txt", "pdf")
        )
        if uploaded_file is not None:
            file_extension = uploaded_file.name.split('.')[-1]
            if file_extension == 'txt':
                document = uploaded_file.read().decode()
            elif file_extension == 'pdf':
                document = extract_text_from_pdf(uploaded_file)
            else:
                st.error("Unsupported file type.")
            st.session_state.question = ""
        else:
            st.info("Please upload a file.")


        # Ask the user for a question via `st.text_area`.
        st.session_state.question = st.text_area(
            "Now ask a question about the document!",
            placeholder="Can you give me a short summary?",
            value=st.session_state.question,  # Use session state to persist question
            disabled=not uploaded_file,
        )

        if uploaded_file and st.session_state.question:
            # Process the uploaded file and question.
            messages = [
                {
                    "role": "user",
                    "content": f"Here's a document: {document} \n\n---\n\n {st.session_state.question}",
                }
            ]

            # Generate an answer using the OpenAI API.
            stream = client.chat.completions.create(
                # b. Change the application to use the LLM (model) “gpt-4o-mini”.
                model="gpt-4o-mini",
                messages=messages,
                stream=True,
            )

            # Stream the response to the app using `st.write_stream`.
            st.write_stream(stream)

    else:
        st.error("Invalid OpenAI API key. Please try again.")