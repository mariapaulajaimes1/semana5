import streamlit as st
from PIL import Image 

st.title("HOLA SOY HUGO")

st.header( "Soy un perro feliz")
st.write ("Este soy yo")

image= Image.open("Hugojaimes.jpeg")
st.image(image,caption= "Hugojaimes")

texto= st.text_input("Escribeme un mensaje", "este es mi mensaje")
st.write( "El mensaje que mandaste es:", texto)

