
import streamlit as st
from chatbot import get_response


st.set_page_config(page_title="Mindmate-Chat", layout="centered")


st.title("🧠 Mindmate-Chat - Your Mental Wellness Friend")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Talk to Mindmate-Chat:", "")  

if st.button("Send") and user_input:
    # Add user message to history
    st.session_state.chat_history.append(("user", user_input))

    # Get response with history passed
    response = get_response(st.session_state.chat_history)

    # Add bot response to history
    st.session_state.chat_history.append(("assistant", response))

# Display chat history
if st.session_state.chat_history:
    st.write("---")
    for role, msg in reversed(st.session_state.chat_history):
        sender = "You" if role == "user" else "Mindmate-Chat"  
        st.markdown(f"**{sender}:** {msg}")


