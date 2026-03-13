import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
df = pd.read_excel("Stock_I.xlsx") 
st.sidebar.header("Filter")
company = st.sidebar.selectbox("Select Company",df["Stock"].unique())
filtered_df = df[df["Stock"] == company]


# Example: Display the dataframe
st.title("Nifty Dashboard")
st.dataframe(filtered_df)

fig = px.line(filtered_df, x="Date", y="Close", "color="Stock", hover_data=["Open", "High", "Low", "Close", "Volume"])
st.plotly_chart(fig)


