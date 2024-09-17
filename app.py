import pandas as pd
import numpy as np
import datetime as date
import scipy.stats as stats
import streamlit as st
import plotly.express as px
import altair as alt


vehicles = pd.read_csv(r"vehicles_us.csv")
median_year=vehicles.groupby(['model'])['model_year'].median()
median_year=median_year.median().round()
median_cylinders=vehicles.groupby(['model'])['cylinders'].median()
median_cylinders=median_cylinders.median().round()
mean_odometer=vehicles.groupby(['model','model_year'])['odometer'].mean()
mean_odometer=mean_odometer.median().round()
vehicles['model_year'] = vehicles['model_year'].fillna(median_year)
vehicles['cylinders'] = vehicles['cylinders'].fillna(median_cylinders)
vehicles['odometer'] = vehicles['odometer'].fillna(mean_odometer)
vehicles['model_year'] = vehicles['model_year'].fillna(median_year)
vehicles['cylinders'] = vehicles['cylinders'].fillna(median_cylinders)
vehicles = vehicles[(vehicles['odometer'] <= vehicles['odometer'].quantile(0.95)) & (vehicles['odometer'] >= vehicles['odometer'].quantile(0.05)) &(vehicles['model_year']<= vehicles['model_year'].quantile(0.95))& (vehicles['model_year']>= vehicles['model_year'].quantile(0.05))] 


st.set_page_config(layout="wide")
st.header("Car advertisments Data:car:")
st.dataframe(vehicles)
option = st.selectbox(
    "select a car model",
   vehicles['model'].unique(),
    placeholder="Select a Car model"
)
model = vehicles[vehicles['model'] == option] 
fig=px.histogram(model['price'])
fig.update_layout( title="Histogram of Car Price v Model",
        xaxis_title="Car Price",
        yaxis_title="Number of Cars" )

scatter = px.scatter(data_frame=model,x='price',y='odometer')
scatter.update_layout( title="Scatter plot miles v price by car model",
        xaxis_title="Car Price",
        yaxis_title="Miles on Car",)

cols = st.columns(2)
 
cols[0].plotly_chart(fig)

cols[1].plotly_chart(scatter)



    