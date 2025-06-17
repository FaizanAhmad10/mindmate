# import streamlit as st
# from chatbot import get_response
# from langchain.schema import HumanMessage, AIMessage

# st.set_page_config(page_title="MindMate", layout="centered")
# st.title("🧠 MindMate - Mental Wellness Chatbot")

# # Initialize session state for chat messages (history)
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Input box
# user_input = st.text_input("How can I help you today?", "")

# # When send button is clicked
# if st.button("Send") and user_input:
#     # Get model response with full history
#     response, updated_history = get_response(user_input, st.session_state.chat_history)
#     st.session_state.chat_history = updated_history

# # Show conversation
# if st.session_state.chat_history:
#     st.write("---")
#     for msg in reversed(st.session_state.chat_history):
#         sender = "🧑 You" if isinstance(msg, HumanMessage) else "🤖 MindMate"
#         st.markdown(f"**{sender}:** {msg.content}")

# # Add clear button
# if st.button("🗑️ Clear Chat"):
#     st.session_state.chat_history = []



import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="PsychBot", layout="centered")
st.title("🧠 PsychBot - Your Mental Wellness Friend")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Talk to PsychBot:", "")

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
        sender = "You" if role == "user" else "PsychBot"
        st.markdown(f"**{sender}:** {msg}")

