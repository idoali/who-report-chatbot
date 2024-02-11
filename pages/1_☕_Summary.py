import streamlit as st 
import json 

st.set_page_config(page_title = "Summary",
                   page_icon = "☕")

with open("docs/summaries.json", "r") as f:
    summaries = json.load(f)
    
st.markdown("# ☕ Report Summary")

for title, text in summaries.items():
    st.markdown(f"### {title}")
    st.markdown(text)
    