import sqlite3
connection = sqlite3.connect("sql/business_performance.db")


import pandas as pd
import sqlite3

items = pd.read_csv("data/raw/olist_order_items_dataset.csv")

connection = sqlite3.connect("sql/business_performance.db")

items.to_sql(
    "fact_order_items",
    connection,
    if_exists="replace",
    index=False
)

result = pd.read_sql(
    "SELECT * FROM fact_order_items LIMIT 5",
    connection
)

print(result)

orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")
reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")

orders.to_sql("dim_orders", connection, if_exists="replace", index=False)

customers.to_sql("dim_customers", connection, if_exists="replace", index=False)

products.to_sql("dim_products", connection, if_exists="replace", index=False)

reviews.to_sql("fact_reviews", connection, if_exists="replace", index=False)

connection.close()


