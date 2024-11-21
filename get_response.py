import streamlit as st

import google.generativeai as genai

def start_chat_session():
    # Fetching the API KEY
    genai.configure(api_key=st.session_state["GOOGLE_API_KEY"])

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    system_instruction = """You are a helpful AI chat assistant. Provide detailed, helpful and meaningful replies to input prompts.
                            The input may contain both text and images. Take the image into context, when it is available. Also use
                            previous chat history for additional context.
                            """
    # Setting model to be used
    model = genai.GenerativeModel("gemini-1.5-flash", generation_config=generation_config,
                                system_instruction=system_instruction)

    # starting chat_session
    chat_session = model.start_chat(
        history=[
        ]
    )

    return chat_session

# Function to convert natural language to SQL
def get_response(input, chat_session):
    response = chat_session.send_message(input, stream=True)
    for chunk in response:
        yield chunk.text 