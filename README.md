# 📊 Sales Performance Dashboard

An interactive web application built with **Python** and **Streamlit** to simulate, analyze, and report e-commerce sales data from a website. This project utilizes the **Pandas** library for data manipulation and **Plotly** for dynamic data visualizations.

🔗 **Live Application:** [👉 Click here to access the Dashboard](https://streamlit.app)

---

## 🚀 Features

- **Dynamic KPI Cards:** Live tracking of Total Revenue, Total Units Sold, and Average Order Value (AOV).
- **Interactive Visualizations:** 
  - *Revenue by Product:* A horizontal bar chart displaying top-performing products.
  - *Daily Revenue Trend:* A time-series line chart illustrating daily financial progression.
- **Custom Filters:** Interactive sidebar to filter metrics and charts by product category instantly.
- **Data Preview:** Expandable section allowing users to inspect and sort raw filtered data rows.

---

## 🛠️ Tech Stack & Libraries

- **Python 3.9+** (Core language)
- **Streamlit** (Web application framework)
- **Pandas** (Data cleaning and aggregation)
- **Plotly Express** (Interactive charting)

---

## 💻 How to Run Locally

If you wish to test or develop this project on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```

2. **Navigate to the project directory:**
   ```bash
   cd sales-analysis-dashboard
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application:**
   ```bash
   streamlit run dashboard.py
   ```

---

## 📂 Project Structure

- `dashboard.py`: Main script containing the Streamlit layout and logic.
- `analise.py` / `gerar_dados.py`: Supporting scripts for data generation and preliminary analysis.
- `requirements.txt`: List of required Python packages.
- `sales.csv` / `vendas.csv`: Datasets utilized by the dashboard application.

---
Developed by **Bárbara Menezes**. Connect with me on [LinkedIn](https://linkedin.com).