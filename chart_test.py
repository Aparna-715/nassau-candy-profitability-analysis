import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Plotly Chart Test")

df = pd.DataFrame({
    "Product": ["Chocolate A", "Chocolate B", "Chocolate C"],
    "Sales": [1200, 950, 700]
})

fig = px.bar(df, x="Product", y="Sales", title="Sample Product Sales")

st.plotly_chart(fig, use_container_width=True)
