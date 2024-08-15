import streamlit as st
from PIL import Image 

st.title("HOLA SOY HUGO")

st.header( "Soy un perro feliz")
st.write ("Este soy yo")

image= Image.open("Hugojaimes.jpeg")
st.image(image,caption= "Hugojaimes")

texto= st.text_input("Escribeme un mensaje", "este es mi mensaje")
st.write( "Gracias por tu mensaje:", texto)

st.subheader("Ahora hablemos un poco")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("correcto!")

with col2:
  st.subheader("Conozcámonos")
  modo = st.radio("¿Qué te consideras?", ("perro", "humano", "otro"))
  if modo == "perro":
    st.write("Hola amigo canino")
  if modo == "humano":
    st.write(" Hola amigo humano")
  if modo == "otro":
     st.write("Hola amigo extraterrestre")


st.subheader("usa los botones")
if st.button(" presiona el botón")
  st.write(" Gracias por presionar")
else:
  st.write(" no has presionado ningun botón")

with st.sidebar:
  st.subheader ("configura la modalidad")
  mod_ radio= st.radio(
    "Escoge la modalidad a usar",
    ("perro", "humano", "otro")
  )
