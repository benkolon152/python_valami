import streamlit as st
import requests

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
        if details and len(politician_name) >=1:
            form_data_dict = {"politician_name": politician_name, "age": age, "party_name": party_name, "color": color, "lie_date": lie_date, "lie_title": lie_title}
            print(f"form_data_dict: {form_data_dict}")

            res = requests.post(url="http://python-valami-zc8q.vercel.app", data=form_data_dict)
            print(f"res.ok: {res.ok}")
            print(f"res.status_code: {res.status_code}")
            print(f"res.text: {res.text}")

            st.success("OK")
        else:
            st.error("Please fill out the form fields.")
    else:
        st.error("Please fill out the form fields.")