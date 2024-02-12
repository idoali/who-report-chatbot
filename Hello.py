import streamlit as st 

# Set page configuration including title and icon
st.set_page_config(page_title="Hello",
                   page_icon="🙏")

# Displaying a markdown header with a welcoming message and description
st.markdown("""
            # 👋 Welcome to World Health Stats 2023!
            Explore the latest insights from the World Health Statistics 2023 Report. Gain valuable insights into global health trends and challenges shaping our world today.
            """)

# Displaying a markdown section with instructions on what users can do
st.markdown("""
            ### 🛠 What You Can Do:
            - Go to `Summary` page to get the summary
            - Go to `Chat` page to ask questions related to the report
            """)
