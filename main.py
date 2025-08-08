import streamlit as st
from langchain_helper import get_chain_from_url

st.set_page_config(page_title="URL + Chat UI", layout="wide")

# Sidebar for URL input
st.sidebar.title("🔗 Input Section")
url = st.sidebar.text_input("Enter a URL:")

# Initialize chain if URL is entered
chain = None
if url:
    chain = get_chain_from_url(url)
    st.sidebar.markdown(f"**URL Entered:** {url}")

# Main title
st.title("💬 Chat Interface")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display message history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input box
user_input = st.chat_input("Say something...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get assistant response via LangChain
    if chain:
        response = chain({"question":user_input})
        response = response.get("answer", "No answer found.")
    else:
        response = "Please enter a valid URL first."

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
