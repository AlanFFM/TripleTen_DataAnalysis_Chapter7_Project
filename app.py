import pandas as pd
import streamlit as st
import plotly.express as px

st.header("Vehicle Advertisement Dashboard")

df = pd.read_csv("vehicles_us.csv")

st.write("This dashboard explores vehicle advertisement data.")

show_raw_data = st.checkbox("Show raw data")

if show_raw_data:
    st.write(df)

st.header("Vehicle Price Distribution")

fig_hist = px.histogram(
    df,
    x="price",
    title="Distribution of Vehicle Prices"
)

st.plotly_chart(fig_hist)

st.header("Price vs. Odometer")

fig_scatter = px.scatter(
    df,
    x="odometer",
    y="price",
    title="Vehicle Price vs. Odometer"
)

st.plotly_chart(fig_scatter)