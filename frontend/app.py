import streamlit as st
import requests

st.title("Code Explanation Chatbot")

code_snippet = st.text_area("Paste your code snippet here:")

if st.button("Get Explanation"):
    if code_snippet:
        response = requests.post("https://chatbot-backend-prasinghal.azurewebsites.net//explain", json={"code": code_snippet})
        if response.status_code == 200:
            explanation = response.json().get("explanation", "No explanation available.")
            st.write("### Explanation:")
            st.write(explanation)
        else:
            st.write("Error: Unable to get explanation from the backend.")
    else:
        st.write("Please enter a code snippet to get an explanation.")