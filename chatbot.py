
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, AIMessage, SystemMessage

load_dotenv()

# Setup the chat model
def get_response(history):
    chat = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile"
    )

    # Base system prompt for tone
    messages = [
        SystemMessage(
            content="You are PsychBot, a compassionate and supportive mental wellness assistant. Answer with empathy and encouragement."
        )
    ]

    # Append chat history as message objects
    for role, msg in history:
        if role == "user":
            messages.append(HumanMessage(content=msg))
        elif role == "assistant":
            messages.append(AIMessage(content=msg))

    # Get latest response
    response = chat(messages)
    return response.content

