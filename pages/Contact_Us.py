import streamlit as st

with st.form(key="email"):
    st.text_input("Your e-mail address:")
    topics = ["Job Inquiries", "Project Proposals", "Other"]
    st.selectbox("What topic do you want to discuss?", topics)
    st.text_area("Your message:")
    st.form_submit_button("Submit")
