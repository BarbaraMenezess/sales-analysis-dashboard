# 📊 Sales Analysis Dashboard

> **An executive sales analytics platform featuring an automated SQLite data ingestion pipeline and quality assertions.**

[![Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
![Python](https://img.shields.io/badge/Python-3.10+-1E3A8A?style=flat&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-In--Memory-003B57?style=flat&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-059669)

---

## 📌 Overview

The **Sales Analysis Dashboard** is an interactive web application built with **Python** and **Streamlit** to simulate, analyze, and report e-commerce sales data. The project incorporates an automated data ingestion pipeline using an in-memory **SQLite** database and **Pandas** for advanced data manipulation, ensuring both clean engineering standards and robust data quality validation.

🔗 **Live Application:** [👉 Click here to access the Dashboard](https://share.streamlit.io)

---

## 🎯 Key Features

- **SQLite Data Ingestion Pipeline**: Uses a lightweight, serverless SQLite in-memory database (`:memory:`) to process and query structured transactional data efficiently.
- **Automated Data Quality & Validation**: Built-in Python assertions (`assert`) validating critical null checks and numerical range rules.
- **Executive Key Performance Indicators (KPIs)**: Real-time calculation of Total Revenue, Units Sold, and Average Order Value (AOV).
- **Interactive Visualizations**: Clean Plotly charts displaying top-performing products and daily sales trends.
- **Custom Filters & Data Preview**: Interactive sidebar to filter metrics by product category and an expandable section to inspect raw data.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Database & Querying**: SQLite (In-Memory), SQL
- **Data Wrangling**: Pandas, NumPy
- **Dashboard & Interface**: [Streamlit](https://streamlit.io/)
- **Data Visualization**: Plotly Express
- **Cloud Deployment**: Streamlit Community Cloud

---

## 🧪 Data Quality & Assertions

To guarantee data reliability before dashboard rendering, the pipeline runs automated tests:
```python
# Example of automated pipeline assertions
assert df_clean['CustomerID'].isnull().sum() == 0, "Missing Customer IDs detected!"
assert (df_clean['Quantity'] > 0).all(), "Invalid quantity values detected!"