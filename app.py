import streamlit as st 
import pandas as pd
import plotly_express as px


car_data = pd.read_csv('vehicles_us.csv') #leo archivo CSV

st.header('titulo aca') #Titulo


hist_button = st.button('Ver histograma') #creo boton

if hist_button: #al clickear en el boton
    #mensajes
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches')
    #crea histograma
    fig = px.histogram(car_data, x='odometer') 
    #hist interactivo
    st.plotly_chart(fig, use_container_width=True)
    
#disp_button = st.button('Ver grafico de dispersión') #creo boton

#if disp_button: #al clickear en el boton
    #mensajes
    #st.write('Creación de un grafico de dipersion para el conjunto de datos de anuncios de venta de coches')
    #crea histograma
    #fig = px.scatter(car_data, x='odometer', y='price') 
    #hist interactivo
    #st.plotly_chart(fig, use_container_width=True)
    

# crear una casilla de verificación
build_dispertion = st.checkbox('Construir un grafico de dispersión')

if build_dispertion: # si la casilla de verificación está seleccionada
    st.write('Construir un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='odometer', y='price') 
    #dispersion interactivo
    st.plotly_chart(fig, use_container_width=True)