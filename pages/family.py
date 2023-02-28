import streamlit as st
from PIL import Image
img = Image.open("пон.jpg")
st.image(img, width=800)