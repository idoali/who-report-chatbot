import streamlit as st 
from utils import make_output, modify_output 

# Set page configuration including title and icon
st.set_page_config(page_title="ChatBot",
                   page_icon="🤔")

# Display the title of the chat interface
st.title("💭 Chat with the Report")

# Initialize session state to store chat messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input in the chat interface
if prompt := st.chat_input("What is your question?"):
    # Display user input as a chat message
    with st.chat_message("user"):
        st.markdown(prompt)
    # Append user input to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get response from the chatbot based on user input
    response = make_output(prompt)
    
    # Display response from the chatbot as a chat message
    with st.chat_message("assistant"):
        # Write response with modified output (if any)
        st.write_stream(modify_output(response))
    # Append chatbot response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
