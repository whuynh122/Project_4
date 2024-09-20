import pandas as pd
import numpy as np
import datetime as date
import scipy.stats as stats
import streamlit as st
import plotly.express as px
import altair as alt

# import data

vehicles = pd.read_csv(r"vehicles_us.csv")
#remove duplicates
vehicles.drop_duplicates(inplace=True)
#preprocess the data

vehicles['model_year'] = vehicles['model_year'].fillna(vehicles.groupby('model')['model_year'].transform('median').round())
vehicles['cylinders'] = vehicles['cylinders'].fillna(vehicles.groupby('model')['cylinders'].transform('median').round())
vehicles['odometer'] = vehicles['odometer'].fillna(vehicles.groupby('model')['odometer'].transform('median').round())
# remove outliers from vehicles
vehicles = vehicles[(vehicles['odometer'] <= vehicles['odometer'].quantile(0.95)) & (vehicles['odometer'] >= vehicles['odometer'].quantile(0.05)) &(vehicles['model_year']<= vehicles['model_year'].quantile(0.95))& (vehicles['model_year']>= vehicles['model_year'].quantile(0.05))] 

# add header to streamlit Project
st.set_page_config(layout="wide")
st.header("Car advertisments Data:car:")
#add dataset to web app
st.dataframe(vehicles)
#select box for vehicle model
option = st.selectbox(
    "select a car model",
   vehicles['model'].unique(),
    placeholder="Select a Car model"
)
model = vehicles[vehicles['model'] == option] 
#histogram of vehicle model and price
fig=px.histogram(model['price'])
fig.update_layout( title="Histogram of Car Price v Model",
        xaxis_title="Car Price",
        yaxis_title="Number of Cars" )
#scatter plot of odometer and price
scatter = px.scatter(data_frame=model,x='price',y='odometer')
scatter.update_layout( title="Scatter plot miles v price by car model",
        xaxis_title="Car Price",
        yaxis_title="Miles on Car",)

cols = st.columns(2)
#ploting both charts
cols[0].plotly_chart(fig)

cols[1].plotly_chart(scatter)



    