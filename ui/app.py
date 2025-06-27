import streamlit as st
import requests

st.set_page_config(page_title="TechCorpGPT", page_icon="🤖")
st.title("TechCorpGPT")

API_ASK_URL = "http://api:8000/chat/ask/"
API_SESSION_URL = "http://api:8000/chat/session/"

# Load session from db
if "messages" not in st.session_state:
    try:
        res = requests.get(API_SESSION_URL)
        res.raise_for_status()
        messages_from_db = res.json()
        
        st.session_state.messages = messages_from_db
    except Exception as e:
        st.session_state.messages = [{"role": "assistant", "message": f"Failed to load messages: {e}"}]

# Save session
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "message": prompt})
    
    try:
        response = requests.post(API_ASK_URL, json={"query": prompt})
        response.raise_for_status()
        data = response.json()
        answer = data.get("answer", "Sorry, I couldn't find an answer.")
    except Exception as e:
        answer = f"Error contacting the API: {e}"
  
    st.session_state.messages.append({"role": "assistant", "message": answer})

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["message"])