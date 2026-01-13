import streamlit as st 
st.title("some static commads lile slider button etc")

age = st.slider("enter your age", 1 , 100)
city = st.selectbox("choose your city", ["delhi","mumbai","pune","chennai","goa"])

if st.button("SHOW DETAILS"):
    st.write("your age is ",age)
    st.write("your city is ",city)