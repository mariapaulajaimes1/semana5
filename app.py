import streamlit as st
from PIL import Image 

st.title("HOLA SOY HUGO")

st.header( "Soy un perro feliz")
st.write ("Este soy yo")

image= Image.open("Hugojaimes.jpeg")
st.image(image,caption= "Hugojaimes")

texto= st.text_input("Escribeme un mensaje", "este es mi mensaje")
st.write( "Gracias por tu mensaje:", texto)

st.subheader("Ahora usemos 2 columnas")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la segunda columna")
  modo= st.radio(" que modalidad es la principal en tu interfaz", ("visual", "auditiva", "tactil"))
  
