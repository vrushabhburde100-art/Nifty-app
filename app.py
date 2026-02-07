import streamlit as st
import pandas as pd

st.title("Nifty Dashboard")

# Load Excel normally
data = pd.read_excel("Stock_I.xlsx")

st.write("Dataset Preview:")
st.dataframe(data)

# If no proper columns, create numeric index chart
try:
    column = st.sidebar.selectbox("Select column", data.columns)
    chart_data = pd.to_numeric(data[column], errors="coerce")
    st.line_chart(chart_data)
except Exception as e:
    st.error("Data format issue. Showing raw data chart instead.")
    st.line_chart(pd.DataFrame(data))
