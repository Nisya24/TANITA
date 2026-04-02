import streamlit as st
st.title('HAPPY BIRTHDAY TANITA')
st.write('Selamat hari lahir ya untuk my teman sahabat dari janin my forever blackpink member. Selamat sdh memulai hidup baru di tahun ke 20 ini, sering-sering ketemuan ya kita. Love you from melbin <3')
slider_value = st.slider('Select a value', min_value=0,max_value=100, value=50)
if (slider_value > 51):
    VIDEO_URL = "https://youtu.be/NndwCpJVurc?si=6eWC5Dy9C7JPARX5"
else:
    VIDEO_URL = "https://youtu.be/NndwCpJVurc?si=6eWC5Dy9C7JPARX5"

st.balloons()
st.video(VIDEO_URL, start_time=2)
