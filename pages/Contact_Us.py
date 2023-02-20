import streamlit as st
import functions

with st.form(key="email"):
    user_email = st.text_input("Your e-mail address:")
    topics = ["Job Inquiries", "Project Proposals", "Other"]
    selected_topic = st.selectbox("What topic do you want to discuss?", topics)
    user_message = st.text_area("Your message:")
    submit_button = st.form_submit_button("Submit")

message = f"""\
Subject: {selected_topic} {user_email}

{user_message}
"""

email_check = functions.check_email(user_email)

if submit_button:
    if email_check == "Invalid e-mail address, please correct.":
        status_message = st.info(email_check)
    else:
        functions.send_email(message)
        status_message = st.info(email_check)
