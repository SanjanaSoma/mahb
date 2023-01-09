import streamlit as st
import pandas as pd
from datetime import time
from datetime import datetime
from PIL import Image


option = st.selectbox(    'Select an airport ',     ('Klia', 'Rgia', 'etc'))
st.write('You selected:', option)
st.write("<h2 style='color:black;'> Heat Map of workers at airport </h2>",
             unsafe_allow_html=True)
from datetime import time
st.write("<h6 style='color:black;'> Date & time selector </h6>",
             unsafe_allow_html=True)
d = st.date_input("Select the date:")
appointment = st.slider(
    "Select the time range:",
    value=(time(11, 30), time(12, 45)))


col1, col2, col3 = st.columns([2,6,1])

with col1:
    st.write("")

with col2:
    img = Image.open("map2.jpeg")
    new_image = img
    st.image(new_image)

with col3:
    st.write("")

st.warning('High Traffic at Check-In Counter', icon="⚠️")

st.write("<h2 style='color:black;'> Real & Estimated wait times </h2>",
             unsafe_allow_html=True)

img2 = Image.open("chart.jpeg")
new_image1 = img2
st.image(new_image1)