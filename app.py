import pandas as pd
import streamlit as st
import plotly.express as px


st.header("Vehicle Advertisement Dashboard")


@st.cache_data
def load_data():
    """Load and lightly clean the vehicle advertisement dataset."""
    df = pd.read_csv("vehicles_us.csv")

    if "is_4wd" in df.columns:
        df["is_4wd"] = df["is_4wd"].fillna(0)

    if "paint_color" in df.columns:
        df["paint_color"] = df["paint_color"].fillna("Unknown")

    if "model_year" in df.columns and "model" in df.columns:
        df["model_year"] = df["model_year"].fillna(
            df.groupby("model")["model_year"].transform("median")
        )
        df["model_year"] = df["model_year"].fillna(df["model_year"].median())

    if "cylinders" in df.columns and "model" in df.columns:
        df["cylinders"] = df["cylinders"].fillna(
            df.groupby("model")["cylinders"].transform("median")
        )
        df["cylinders"] = df["cylinders"].fillna(df["cylinders"].median())

    if "odometer" in df.columns and "model" in df.columns and "model_year" in df.columns:
        df["odometer"] = df["odometer"].fillna(
            df.groupby(["model", "model_year"])["odometer"].transform("median")
        )
        df["odometer"] = df["odometer"].fillna(
            df.groupby("model")["odometer"].transform("median")
        )
        df["odometer"] = df["odometer"].fillna(df["odometer"].median())

    return df


df = load_data()

st.write(
    "This dashboard explores used vehicle advertisement data, including vehicle prices, mileage, and condition."
)

exclude_expensive = st.checkbox(
    "Exclude vehicles priced above $100,000",
    value=True
)

if exclude_expensive:
    chart_df = df[df["price"] <= 100000]
    st.write("Charts currently exclude vehicles priced above $100,000.")
else:
    chart_df = df
    st.write("Charts currently include all vehicles, including expensive outliers.")

st.header("Vehicle Price Distribution")

fig_hist = px.histogram(
    chart_df,
    x="price",
    nbins=50,
    title="Distribution of Vehicle Prices"
)
st.plotly_chart(fig_hist, use_container_width=True)

st.header("Price vs. Odometer")

fig_scatter = px.scatter(
    chart_df,
    x="odometer",
    y="price",
    title="Vehicle Price vs. Odometer",
    opacity=0.5
)
st.plotly_chart(fig_scatter, use_container_width=True)

show_raw_data = st.checkbox("Show raw cleaned data")

if show_raw_data:
    st.write(chart_df)
