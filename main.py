import streamlit as st
name = st.text_input("Enter your name :")
fname = st.text_input("Enter your Father Name ")
adr = st.text_area("enter your Text")
classdata = st.selectbox("Select your Class:",("FYCM","SYCM","TYCM"))

button = st.button("Submit")
if button :
    st.markdown(f"""Name : {name} Father name : {fname} address :{adr} class :{classdata}""")