import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ── 1. Load Data ──────────────────────────────────────────────
df = pd.read_csv("sales_data.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)

print("Dataset loaded successfully!")
print(df.head())
print(f"\nTotal Records: {len(df)}")

# ── 2. Total Sales ─────────────────────────────────────────────
total_sales = df["TotalSales"].sum()
print(f"\n✅ Total Sales Revenue: ₹{total_sales:,}")

# ── 3. Product-wise Sales ──────────────────────────────────────
product_sales = df.groupby("Product")["TotalSales"].sum().sort_values(ascending=False)
print("\nProduct-wise Sales:\n", product_sales)

# ── 4. Region-wise Sales ───────────────────────────────────────
region_sales = df.groupby("Region")["TotalSales"].sum().sort_values(ascending=False)
print("\nRegion-wise Sales:\n", region_sales)

# ── 5. Monthly Trend ───────────────────────────────────────────
monthly_sales = df.groupby("Month")["TotalSales"].sum()
print("\nMonthly Sales Trend:\n", monthly_sales)

# ── 6. Payment Status ──────────────────────────────────────────
payment_status = df["PaymentStatus"].value_counts()
print("\nPayment Status Distribution:\n", payment_status)

# ══════════════════════════════════════════════════════════════
# GRAPHS
# ══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Sales Data Analysis — O2C Process", fontsize=16, fontweight="bold", y=1.01)

colors_bar  = ["#4e79a7", "#f28e2b", "#59a14f", "#e15759", "#76b7b2"]
colors_pie  = ["#4e79a7", "#f28e2b", "#e15759"]
colors_line = "#4e79a7"

# Graph 1: Product-wise Bar Chart
ax1 = axes[0, 0]
product_sales.plot(kind="bar", ax=ax1, color=colors_bar[:len(product_sales)], edgecolor="white")
ax1.set_title("Product-wise Sales Revenue", fontweight="bold")
ax1.set_xlabel("Product")
ax1.set_ylabel("Total Sales (₹)")
ax1.tick_params(axis="x", rotation=30)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{int(x):,}"))
ax1.grid(axis="y", linestyle="--", alpha=0.5)

# Graph 2: Region-wise Bar Chart
ax2 = axes[0, 1]
region_sales.plot(kind="bar", ax=ax2, color=colors_bar[:len(region_sales)], edgecolor="white")
ax2.set_title("Region-wise Sales Revenue", fontweight="bold")
ax2.set_xlabel("Region")
ax2.set_ylabel("Total Sales (₹)")
ax2.tick_params(axis="x", rotation=30)
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{int(x):,}"))
ax2.grid(axis="y", linestyle="--", alpha=0.5)

# Graph 3: Monthly Trend Line Chart
ax3 = axes[1, 0]
monthly_sales.plot(kind="line", ax=ax3, color=colors_line, marker="o", linewidth=2)
ax3.set_title("Monthly Sales Trend (2024)", fontweight="bold")
ax3.set_xlabel("Month")
ax3.set_ylabel("Total Sales (₹)")
ax3.tick_params(axis="x", rotation=45)
ax3.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{int(x):,}"))
ax3.grid(axis="y", linestyle="--", alpha=0.5)

# Graph 4: Payment Status Pie Chart
ax4 = axes[1, 1]
payment_status.plot(kind="pie", ax=ax4, colors=colors_pie,
                    autopct="%1.1f%%", startangle=90,
                    wedgeprops={"edgecolor": "white", "linewidth": 1.5})
ax4.set_title("Payment Status Distribution", fontweight="bold")
ax4.set_ylabel("")

plt.tight_layout()
plt.savefig("sales_analysis_graphs.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n✅ Graphs saved as 'sales_analysis_graphs.png'")