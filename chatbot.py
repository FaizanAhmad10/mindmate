# import streamlit as st
# from langchain_groq import ChatGroq
# from langchain.schema import HumanMessage, AIMessage, SystemMessage

# def get_chat_model():
#     return ChatGroq(
#         groq_api_key="GROQ_API_KEY",
#         model="gemma2-9b-it"
#     )


# def get_response(user_input, chat_history):
#     model = get_chat_model()
#     # Add a system message only once at the beginning
#     if not chat_history or not isinstance(chat_history[0], SystemMessage):
#         chat_history.insert(0, SystemMessage(content="You are a kind and empathetic mental wellness assistant named MindMate. Be supportive and respectful in your responses."))

#     messages = chat_history + [HumanMessage(content=user_input)]
#     response = model(messages)

#     chat_history.append(HumanMessage(content=user_input))
#     chat_history.append(AIMessage(content=response.content))
#     return response.content, chat_history


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

