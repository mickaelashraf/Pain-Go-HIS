import streamlit as st
import requests

st.title("Pain & Go HIS")

query = st.text_input("Enter your query:")
if st.button("Submit"):
    response = requests.post("http://127.0.0.1:5000/query", json={"query": query})
    st.write(response.json()["answer"])