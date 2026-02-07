import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Stock_I.xlsx") 

# Example: Display the dataframe
st.title("Nifty Dashboard")
st.dataframe(df)

# Example: Plot closing prices
st.line_chart(df['Close'])  


