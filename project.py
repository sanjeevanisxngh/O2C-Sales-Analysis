import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create Month column
df["Month"] = df["Order_Date"].dt.strftime("%b")

# Show data
print("Dataset Preview:")
print(df.head())
print()

# Total sales
total_sales = df["Total_Sales"].sum()
print("Total Sales:", total_sales)

# Average order value
avg_order_value = df["Total_Sales"].mean()
print("Average Order Value:", avg_order_value)

# Product-wise sales
product_sales = df.groupby("Product")["Total_Sales"].sum()
print("\nSales by Product:")
print(product_sales)

# Region-wise sales
region_sales = df.groupby("Region")["Total_Sales"].sum()
print("\nSales by Region:")
print(region_sales)

# Payment status count
payment_status = df["Payment_Status"].value_counts()
print("\nPayment Status:")
print(payment_status)

# Monthly sales
monthly_sales = df.groupby("Month")["Total_Sales"].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# Graph 1: Product Sales
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Graph 2: Region Sales
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Graph 3: Payment Status
plt.figure(figsize=(6, 6))
payment_status.plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Status Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Graph 4: Monthly Sales Trend
plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()