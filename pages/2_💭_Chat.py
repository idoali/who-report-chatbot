import streamlit as st 
from utils import make_output, modify_output 

st.set_page_config(page_title = "ChatBot",
                   page_icon = "🤔")

st.title("💭 Chat with the Report")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
if prompt := st.chat_input("What is your question?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = make_output(prompt)
    
    with st.chat_message("assistant"):
        st.write_stream(modify_output(response))
    st.session_state.messages.append({"role": "assistant", "content": response})