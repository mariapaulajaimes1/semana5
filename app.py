import streamlit as st
from PIL import Image 

st.title("TITULO PÁGINA")

st.header( "Hola, cómo va todo")
st.write ("Diferentes tipos de letra")
image= Image.open(Hugojaimes.jpeg)

st.image(image,caption= "Hugojaimes")
