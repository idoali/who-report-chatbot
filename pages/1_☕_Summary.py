import streamlit as st 
import json 

# Set page configuration including title and icon
st.set_page_config(page_title="Summary",
                   page_icon="☕")

# Load summary data from a JSON file
with open("docs/summaries.json", "r") as f:
    summaries = json.load(f)
    
# Display a markdown header for the report summary
st.markdown("# ☕ Report Summary")

# Iterate over each title and corresponding text in the summaries
for title, text in summaries.items():
    # Display each title as a markdown sub-header
    st.markdown(f"### {title}")
    # Display the text associated with the title
    st.markdown(text)
