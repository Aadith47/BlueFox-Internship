# ASSIGNMENT 2: Sales Data Analysis with GroupBy

import pandas as pd

#Create the sales DataFrame
data = {
    "product": ["Laptop", "Mouse", "Notebook", "Pen", "Phone", "Eraser"],
    "category": ["Electronics", "Electronics", "Stationery", "Stationery", "Electronics", "Stationery"],
    "quantity": [5, 20, 50, 100, 8, 30],
    "price": [50000, 500, 40, 10, 30000, 15],
}

df = pd.DataFrame(data)
print(df)

#1. Add a column "total_sales" = quantity * price
df["total_sales"] = df["quantity"] * df["price"]
print(df)

#2. Group by "category" and calculate aggregations
category_summary = df.groupby("category").agg(
    total_quantity=("quantity", "sum"),
    average_price=("price", "mean"),
    product_count=("product", "count"),
)
print(category_summary)

#3. Find the category with the highest total sales

category_total_sales = df.groupby("category")["total_sales"].sum()
top_category = category_total_sales.idxmax()

print(f"{top_category}  →  ₹{category_total_sales[top_category]:,}")

#4. Display products sorted by total_sales (descending)
sorted_df = df.sort_values("total_sales", ascending=False)
print(sorted_df.to_string(index=False))
