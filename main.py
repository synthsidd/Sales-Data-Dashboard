# Sales Data Dashboard
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the sales data
data = pd.read_csv("sales_data.csv", parse_dates=["Date"])

# Add new columns
data["Revenue"] = data["Quantity"] * data["UnitPrice"]
data["Month"] = data["Date"].dt.to_period("M")

# Summary metrics
total_revenue = data["Revenue"].sum()
total_orders = data["OrderID"].nunique()
total_units = data["Quantity"].sum()
average_order = total_revenue / total_orders

# Show key numbers
print("----- Sales Summary -----")
print(f"Total Revenue: ₹{total_revenue}")
print(f"Total Orders: {total_orders}")
print(f"Total Units Sold: {total_units}")
print(f"Average Order Value: ₹{round(average_order, 2)}\n")

# Monthly Revenue Trend
monthly = data.groupby("Month")["Revenue"].sum()
monthly.plot(kind="line", marker="o", title="Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 5 Products
top_products = data.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)
top_products.plot(kind="bar", color="skyblue", title="Top 5 Products by Revenue")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.show()

# Revenue by Category
category = data.groupby("Category")["Revenue"].sum()
sns.barplot(x=category.index, y=category.values, palette="Set2")
plt.title("Revenue by Category")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.show()

# Revenue by Region
region = data.groupby("Region")["Revenue"].sum()
region.plot(kind="pie", autopct="%1.1f%%", title="Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()
