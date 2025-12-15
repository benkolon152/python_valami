import streamlit as st

st.set_page_config(page_title="Lies page", layout="wide")
st.title("Lies Form")

with st.form(key="my-form"):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Politician")
        politician_name = st.text_input("Name", placeholder="Johnny Laser")
        age = st.number_input("Age", step=1, min_value=18)
    with col2:
        st.subheader("Party")
        party_name = st.selectbox("Name", ["Fadisz", "Duna", "DéKÁ", "MKKP", "Momentum", "MSZP", "Jobbik", "LMP", "DK"])
        color = st.color_picker("Color", "#FF6A00")
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Lie")
        lie_date = st.date_input("Date", "today")
        lie_title = st.text_area("Lie")
    with col4:
        st.subheader("Details")
        details = st.checkbox("Yes, I really want to store these data!")
    
    submit = st.form_submit_button()
    if submit:
        st.success("OK")
    else:
        st.error("Please fill out the form fields.")