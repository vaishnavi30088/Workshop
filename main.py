import streamlit as st


name = st.text_input("Enter your name", "John Doe")
password = st.text_input("Enter your password", type="password")


if st.button("Submit"):
   if len(password) < 8:
       st.warning("Password must be at least 8 characters long")


   st.success("Password is valid")


