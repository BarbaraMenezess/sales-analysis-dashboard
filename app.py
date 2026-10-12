import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# 1. Configuração da Página com design executivo off-white
st.set_page_config(
    page_title="Sales Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# Estilização customizada (Fundo off-white #FDFBF7 e paleta navy/slate blue)
st.markdown("""
    <style>
    .stApp {
        background-color: #FDFBF7;
    }
    h1, h2, h3 {
        color: #1E3A8A;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Pipeline de Ingestão de Dados com SQLite em Memória
@st.cache_data
def load_data():
    data = {
        'InvoiceNo': ['536365', '536366', '536367', '536368', '536369', '536370', '536371', '536372'],
        'StockCode': ['85123A', '71053', '84406B', '84029G', '84029E', '22752', '21730', '22633'],
        'Description': ['WHITE HANGING HEART T-LIGHT HOLDER', 'WHITE METAL LANTERN', 'CREAM CUPID HEARTS COAT HANGER', 'KNITTED UNION FLAG HOT WATER BOTTLE', 'RED WOOLLY HOTTIE WHITE HEART.', 'SET 7 BABUSHKA NESTING BOXES', 'GLASS STAR FROSTED T-LIGHT HOLDER', 'HAND WARMER UNION JACK'],
        'Quantity': [6, 6, 8, 6, 6, 2, 6, 6],
        'InvoiceDate': ['2023-10-01', '2023-10-01', '2023-10-02', '2023-10-02', '2023-10-03', '2023-10-03', '2023-10-04', '2023-10-04'],
        'UnitPrice': [2.55, 3.39, 2.75, 3.39, 3.39, 7.65, 4.25, 1.85],
        'CustomerID': [17850, 17850, 13047, 13047, 13047, 12837, 12837, 17850],
        'Category': ['Decor', 'Decor', 'Home', 'Apparel', 'Apparel', 'Gifts', 'Decor', 'Gifts']
    }
    df = pd.DataFrame(data)
    
    conn = sqlite3.connect(':memory:')
    df.to_sql('sales_raw', conn, index=False, if_exists='replace')
    
    query = "SELECT * FROM sales_raw WHERE Quantity > 0 AND UnitPrice > 0"
    df_clean = pd.read_sql(query, conn)
    conn.close()
    
    # Validação de dados assertiva
    assert df_clean['CustomerID'].isnull().sum() == 0, "Missing Customer IDs detected!"
    
    df_clean['Revenue'] = df_clean['Quantity'] * df_clean['UnitPrice']
    df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])
    
    return df_clean

df = load_data()

# 3. Cabeçalho do Dashboard
st.title("📊 Sales Analysis Dashboard")
st.markdown("An executive sales analytics platform featuring an automated SQLite data ingestion pipeline and quality assertions.")
st.markdown("---")

# 4. Filtros na Barra Lateral
st.sidebar.header("Filter Options")
selected_category = st.sidebar.selectbox("Select Product Category", options=["All"] + list(df['Category'].unique()))

if selected_category != "All":
    df_filtered = df[df['Category'] == selected_category]
else:
    df_filtered = df

# 5. KPIs Executivos com Ticket Médio por Fatura (InvoiceNo) rigoroso
total_revenue = df_filtered['Revenue'].sum()
total_units = df_filtered['Quantity'].sum()
# Cálculo rigoroso de AOV agrupado por InvoiceNo
invoice_totals = df_filtered.groupby('InvoiceNo')['Revenue'].sum()
aov = invoice_totals.mean() if not invoice_totals.empty else 0.0

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Units Sold", f"{total_units:,}")
col3.metric("Average Order Value (AOV)", f"${aov:,.2f}")

st.markdown("---")

# 6. Gráficos Interativos (Plotly com chamada limpa st.plotly_chart)
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Top Products by Revenue")
    product_rev = df_filtered.groupby('Description')['Revenue'].sum().reset_index().nlargest(5, 'Revenue')
    fig_prod = px.bar(product_rev, x='Revenue', y='Description', orientation='h', color='Revenue', color_continuous_scale='Blues')
    fig_prod.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_prod, use_container_width=True)

with col_chart2:
    st.subheader("Daily Revenue Trend")
    daily_rev = df_filtered.groupby('InvoiceDate')['Revenue'].sum().reset_index()
    fig_time = px.line(daily_rev, x='InvoiceDate', y='Revenue', markers=True, line_shape='spline')
    fig_time.update_traces(line_color='#1E3A8A', marker_size=8)
    fig_time.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_time, use_container_width=True)

# 7. Tabela de Dados Detalhados
with st.expander("🔍 Inspect Filtered Raw Data"):
    st.dataframe(df_filtered, use_container_width=True)