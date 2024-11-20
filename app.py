import streamlit as st
from PIL import Image

from get_response import get_response

# Streamlit app

# Title
st.set_page_config(page_title="AskBOT")

# Header
st.title("Current Thread")

# Initializing chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat messages from history on app rerun
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Sidebar for text input and image upload
with st.sidebar.form(key="chat_form", clear_on_submit=True):
    st.header("Image Upload")
    # Get Image input from user
    file_object = st.file_uploader("Upload your File", type=["jpg", "jpeg", "png"])
    # Submit Button
    submit_file = st.form_submit_button("Send")

text = st.chat_input(placeholder="AMA!")

# React to user input
if submit_file or text:
        input = []
        # If prompt has a file attachment
        if submit_file and file_object:
            # Extract image file from the attached file_object
            file = Image.open(file_object)
            # Content to be given to Model
            input.append(file)
            # Display user message in chat message container
            st.chat_message("user").image(file)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": file})
        # If prompt is only text
        if text:
            # Content to be given to Model
            input.append(text)
            # Display user message in chat message container
            st.chat_message("user").markdown(text)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": text})

        # Get response
        response = st.chat_message("assistant").write_stream(get_response(input))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})