import pandas as pd
import numpy as np
import datetime as date
import scipy.stats as stats
import streamlit as st
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt

vehicles = pd.read_csv(r"vehicles_us.csv")

st.set_page_config(layout="wide")
st.header("Car advertisments Data:car:")
st.dataframe(vehicles)
option = st.selectbox(
    "select a car model",
   vehicles['model'].unique(),
   index=None,
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


    