import streamlit as st

st.title("Welcome to Streamlit App")

a = st.number_input("Enter no 1")
b = st.number_input("Enter no 2")

V = st.selectbox("Select Operation", ["Addition", 
                                  "Subtraction", 
                                  "Multiplication", 
                                  "Division"])

if st.button("Calculate"):
    if V == "Addition":
        st.write("Result: ", a + b)
    if V == "Subtraction":
        st.write("Result: ", a - b)
    if V == "Multiplication":
        st.write("Result: ", a * b)
    if V == "Division":
        if b != 0:
            st.write("Result: ", a / b)
        else:
            st.write("Error: Division by zero is not allowed.")