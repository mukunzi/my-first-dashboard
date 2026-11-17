import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Title of the dashboard
st.title("Beginner Store Sales Dashboard")

# 2. Data (A simple table created right inside Python)
data = {
    "city": ["Kigali", "Gisenyi", "Huye", "Musanze", "Ngororero", "Karongi", "Muhanga", "Rwamagana"],
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop", "Mouse", "Keyboard", "Monitor"],
    "sales": [100, 200, 300, 400, 150, 250, 350, 450],
    "unity_price": [10, 20, 30, 40, 15, 25, 35, 45]
}
df = pd.DataFrame(data)

# 3. Filter (Combine "All" + all unique cities into ONE dropdown)
city_options = ["All"] + list(df["city"].unique())
selected_city = st.selectbox("Choose a city:", options=city_options)

if selected_city != "All":
    df = df[df["city"] == selected_city]

# 4. Visuals (Aligned all the way to the left so they ALWAYS show!)
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df['sales'].sum():,}")
col2.metric("Total Products Sold", f"{df['product'].nunique()}")
col3.metric("Average Unity Price", f"${df['unity_price'].mean():.2f}")

fig = px.bar(df, x="product", y="sales", color="city", barmode="group", title="Sales by Product and City")
st.plotly_chart(fig)
st.dataframe(df)
