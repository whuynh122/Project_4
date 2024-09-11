import pandas as pd
import numpy as np
import datetime as date
import scipy.stats as stats
import streamlit as st
import plotly.express as px
import altair as alt

vehicles = pd.read_csv(r"vehicles_us.csv")
st.dataframe(vehicles)