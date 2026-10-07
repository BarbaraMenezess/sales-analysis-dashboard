import pandas as pd
import plotly.express as px
import streamlit as st

# Set web page configuration
st.set_page_config(
    page_title="Sales Performance Dashboard", page_icon="📊", layout="wide"
)

# 1. Load data
try:
    df = pd.read_csv("sales.csv")
    df["Date"] = pd.to_datetime(df["Date"])
except FileNotFoundError:
    st.error(
        "❌ 'sales.csv' not found. Please run 'generate_data.py' script first."
    )
    st.stop()

# Header
st.title("📊 Sales Performance Dashboard")
st.markdown("Interactive overview of company financial and product metrics.")
st.markdown("---")

# 2. Sidebar Filters
st.sidebar.header("Filter Options")
categories = ["All"] + list(df["Category"].unique())
selected_category = st.sidebar.selectbox("Select Category:", categories)

# Apply filter if specific category is chosen
if selected_category != "All":
    df_filtered = df[df["Category"] == selected_category]
else:
    df_filtered = df

# 3. KPI Top Row Cards
total_revenue = df_filtered["Total_Sales"].sum()
total_units = df_filtered["Quantity"].sum()
average_ticket = df_filtered["Total_Sales"].mean()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="💰 Total Revenue", value=f"${total_revenue:,.2f}")

with col2:
    st.metric(label="📦 Total Units Sold", value=f"{total_units:,}")

with col3:
    st.metric(label="🎟️ Average Order Value (AOV)", value=f"${average_ticket:,.2f}")

st.markdown("---")

# 4. Interactive Charts Layout
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Revenue by Product")
    # Group and sort data for the bar chart
    product_data = (
        df_filtered.groupby("Product")["Total_Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Total_Sales", ascending=True)
    )

    fig_bar = px.bar(
        product_data,
        x="Total_Sales",
        y="Product",
        orientation="h",
        labels={"Total_Sales": "Revenue ($)", "Product": "Product"},
        template="plotly_white",
        color="Total_Sales",
        color_continuous_scale="Viridis",
    )
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

with right_chart:
    st.subheader("Daily Revenue Trend")
    # Group data by date for line chart
    daily_sales = (
        df_filtered.groupby("Date")["Total_Sales"].sum().reset_index()
    )

    fig_line = px.line(
        daily_sales,
        x="Date",
        y="Total_Sales",
        labels={"Total_Sales": "Daily Revenue ($)", "Date": "Date"},
        template="plotly_white",
    )
fig_line.update_traces(line=dict(color="#2b5c8f", width=2))
    st.plotly_chart(fig_line, use_container_width=True)

# 5. Data Preview Section
with st.expander("👀 View Raw Filtered Data Table"):
    st.dataframe(df_filtered.sort_values(by="Date", ascending=False), use_container_width=True)
