import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load sample dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    return pd.read_csv(url)

df = load_data()

# App title
st.title("EDA Histogram App")
st.write("Explore the distribution of numeric variables in the Tips dataset.")

# Sidebar inputs
st.sidebar.header("Controls")

numeric_columns = df.select_dtypes('number').columns
selected_var = st.sidebar.selectbox("Select Variable", numeric_columns)
bins = st.sidebar.slider("Number of Bins", 5, 50, 20)

# Histogram
st.subheader(f"Histogram of {selected_var}")
fig, ax = plt.subplots()
ax.hist(df[selected_var], bins=bins, color="steelblue", edgecolor="white")
ax.set_xlabel(selected_var)
ax.set_ylabel("Count")
st.pyplot(fig)

# Summary statistics
st.subheader("Summary Statistics")
st.write(df[selected_var].describe())