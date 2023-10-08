import streamlit as st
from PIL import Image

# 画像
image = Image.open('./data/python_logo.png')
st.image(image, width=300)