import streamlit as st
from dotenv import load_dotenv
load_dotenv
import google.generativeai as genai
import os
from PIL import Image
import pathlib
import textwrap
# configuring the key
genai.configure(api_key = os.getenv('GOOGLE-API-KEY'))
#Page for image to tect
st.header('Gemini Image to Text Application')
input = st.text_input('Input Prompt',key = 'input')
uploaded_img = st.file_uploader('Upload the image',
                                type = ['jpg','png','jpeg'])
# Display the image
image = ''
if uploaded_img is not None:
    image = Image.open(uploaded_img)
    st.image(image,caption = 'Image uploaded',use_column_width = True)
    