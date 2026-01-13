import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBSCBS4FlyS022uD8W_zg5Dv_rcebNe6m4")
model = genai.GenerativeModel("models/gemini-2.5-flash")
user_input = st.text_input("Enter your prompt:")
if user_input:
    response = model.generate_content(user_input)
    st.write("AI Response: ", response.text)