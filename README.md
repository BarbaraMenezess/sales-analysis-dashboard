# 📊 Sales Analysis Dashboard

> **An executive sales analytics platform featuring an automated SQLite data ingestion pipeline and production-grade data quality validation.**

[![Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
![Python](https://img.shields.io/badge/Python-3.10+-1E3A8A?style=flat&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-In--Memory-003B57?style=flat&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-059669)

---

## 📌 Overview

The **Sales Analysis Dashboard** is an interactive web application built with **Python**, **Pandas**, and **Streamlit**. It processes transactional sales records through an in-memory **SQLite** pipeline, running automated checks and aggregating executive metrics for real-time decision-making.

🔗 **Live Application:** [👉 Access the Dashboard on Streamlit Cloud](https://share.streamlit.io) *(Configure with your exact app URL)*

---

## 🎯 Key Features

- **SQLite In-Memory Pipeline**: Loads and queries structured transactional records efficiently using SQL clauses.
- **Robust Data Validation**: Replaces simple assertions with user-facing production safeguards (checking empty states and missing identifiers).
- **Executive Key Performance Indicators (KPIs)**: Real-time computation of Total Revenue, Total Units Sold, and rigorous Average Order Value (AOV) grouped by invoice.
- **Interactive Visualizations**: Clean Plotly charts displaying top-performing products by revenue and daily sales trends.
- **Custom Filters & Raw Data Inspector**: Dynamic category filtering and an expandable data table view.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Database**: SQLite (In-Memory)
- **Data Wrangling**: Pandas, NumPy
- **Interface & Dashboard**: Streamlit
- **Visualization**: Plotly Express

---

## 🚀 Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/BarbaraMenezess/sales-analysis-dashboard.git](https://github.com/BarbaraMenezess/sales-analysis-dashboard.git)
   cd sales-analysis-dashboard