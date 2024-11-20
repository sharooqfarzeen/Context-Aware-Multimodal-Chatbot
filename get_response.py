import os
from dotenv import load_dotenv

import google.generativeai as genai

# Loading all environment variables
load_dotenv()

# Fetching the API KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

system_instruction = """You are a helpful AI chat assistant. Provide detailed, helpful and meaningful replies to input prompts.
                        The input may contain both text and images. Take the image into context, when it is available. Also use
                        previous chat history for additional context.
                        """
# Setting model to be used
model = genai.GenerativeModel("gemini-1.5-flash",
                             system_instruction=system_instruction)

# starting chat_session
chat_session = model.start_chat()

# Function to convert natural language to SQL
def get_response(input, chat=chat_session):
    response = chat.send_message(input, stream=True)
    for chunk in response:
        yield chunk.text 