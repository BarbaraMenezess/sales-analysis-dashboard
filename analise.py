import pandas as pd

# 1. Load the generated dataset
try:
    df = pd.read_csv('sales.csv')
    print("📊 Data loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: The file 'sales.csv' was not found. Please run 'generate_data.py' first.")
    exit()

# 2. Dataset preview
print("--- First Rows of the Dataset ---")
print(df.head(), "\n")

# 3. Overall Metrics (Total Revenue and Total Units Sold)
total_revenue = df['Total_Sales'].sum()
total_units_sold = df['Quantity'].sum()

print("--- Overall Financial Metrics ---")
print(f"💰 Total Revenue: ${total_revenue:,.2f}")
print(f"📦 Total Units Sold: {total_units_sold} units\n")

# 4. Performance by Product (Revenue and Quantity Ordered)
print("--- Product Performance ---")
product_analysis = df.groupby('Product').agg(
    Units_Sold=('Quantity', 'sum'),
    Total_Revenue=('Total_Sales', 'sum')
).sort_values(by='Total_Revenue', ascending=False)

print(product_analysis.to_string(), "\n")

# 5. Average Ticket Price (AOV)
average_ticket = df['Total_Sales'].mean()
print("--- Average Order Value (AOV) ---")
print(f"🎟️ Average value per order: ${average_ticket:,.2f}\n")


