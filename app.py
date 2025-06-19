import streamlit as st 
import pandas as pd
import plotly_express as px


car_data = pd.read_csv('vehicles_us.csv') #leo archivo CSV

st.header('Análisis de datos de venta de coches') #Titulo

price_button = st.button('Precio de los autos') #creo boton y le doy nombre

if price_button: #al clickear en el boton
    #mensaje que aparece encima del gráfico
    st.write('Precio de los autos')
    #crea histograma
    fig = px.histogram(car_data, x='price') 
    #hist interactivo
    st.plotly_chart(fig, use_container_width=True)


odom_button = st.button('Kilometraje de los autos') #creo boton y le doy nombre

if odom_button: #al clickear en el boton
    #mensaje que aparece encima del gráfico
    st.write('Kilometraje de los autos')
    #crea histograma
    fig = px.histogram(car_data, x='odometer') 
    #hist interactivo
    st.plotly_chart(fig, use_container_width=True)
    

# crear una casilla de verificación
price_odom = st.checkbox('Relación kilometraje - precio')

if price_odom: # si la casilla de verificación está seleccionada
    #mensaje que aparece encima del gráfico
    st.write('Relación precio - kilometraje')
    fig = px.scatter(car_data, x='odometer', y='price') 
    #dispersion interactivo
    st.plotly_chart(fig, use_container_width=True)


cond_button = st.button('Condición de los autos') #creo boton y le doy nombre

if cond_button: #al clickear en el boton
    #mensaje que aparece encima del gráfico
    st.write('Condición de los autos')
    #crea histograma
    fig = px.histogram(car_data, x='condition') 
    #hist interactivo
    st.plotly_chart(fig, use_container_width=True)
    
    
cond_price_button = st.checkbox('Relación condición - precio') #creo checkbox

if cond_price_button: #al clickear en el boton
    #mensaje que aparece encima del gráfico
    st.write('Relación precio - condición del auto')
    #crea grafico de dispersion
    fig = px.scatter(car_data, x='condition', y='price') 
    #graf de dipersion interactivo
    st.plotly_chart(fig, use_container_width=True)
    
odom_cond_button = st.checkbox('Relación kilometraje - condición') # creo checkbox

if odom_cond_button:
    #mensaje que aparece encima del gráfico
    st.write('Relación condición - kilometraje del auto')
    #crea grafico de dispersion
    fig = px.scatter(car_data, x='odometer', y='condition') 
    #graf de dispersión interactivo
    st.plotly_chart(fig, use_container_width=True)
    
    
year_button = st.button('Modelo según año') #creo boton

if year_button: #al clickear en el boton
    #mensaje que aparece encima del gráfico
    st.write('Modelo según año')
    #crea histograma
    fig = px.histogram(car_data, x='model_year') 
    #hist interactivo
    st.plotly_chart(fig, use_container_width=True)
    


year_condition = st.checkbox('Relación año del auto - condición') #creo checkbox

if year_condition: # si la casilla de verificación está seleccionada
    #mensaje que aparece encima del gráfico
    st.write('Relación año del auto - condición')
    #creo grafico de dispersion
    fig = px.scatter(car_data, x='model_year', y='condition') 
    #dispersion interactivo
    st.plotly_chart(fig, use_container_width=True)
    
year_price = st.checkbox('Relación año del auto - precio') #creo checkbox

if year_price: # si la casilla de verificación está seleccionada
    #mensaje que aparece encima del gráfico
    st.write('Relación año del auto - precio')
    #histograma
    fig = px.histogram(car_data, x='model_year', y='price') 
    #dispersion interactivo
    st.plotly_chart(fig, use_container_width=True)
    
listed_button = st.button('Cantidad de días en el mercado') #creo boton

if listed_button: #al clickear en el boton
    #mensaje que aparece encima del gráfico
    st.write('Cantidad de días en el mercado')
    #crea histograma
    fig = px.histogram(car_data, x='days_listed') 
    #hist interactivo
    st.plotly_chart(fig, use_container_width=True)

listed_condition = st.checkbox('Relación condición del auto - dias en el mercado') #creo checkbox

if listed_condition: # si la casilla de verificación está seleccionada
    #mensaje que aparece encima del gráfico
    st.write('Relación condición del auto - dias en el mercado')
    #grafico de dispersion
    fig = px.scatter(car_data, y='days_listed', x='condition') 
    #dispersion interactivo
    st.plotly_chart(fig, use_container_width=True)
    

listed_price = st.checkbox('Relación precio - dias en el mercado') #creo checkbox con nombre

if listed_price: # si la casilla de verificación está seleccionada se crea el gráfico
    #mensaje que aparece encima del gráfico
    st.write('Relación precio - dias en el mercado')
    #grafico de dispersion
    fig = px.scatter(car_data, x='days_listed', y='price') 
    #grafico de dispersión
    st.plotly_chart(fig, use_container_width=True)