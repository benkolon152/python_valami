import streamlit as st

st.set_page_config(page_title="Lies page", layout="wide")
st.title("Lies Form")

with st.form(key="my-form"):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Politician")
    with col2:
        st.subheader("Party")
    
    submit = st.form_submit_button()