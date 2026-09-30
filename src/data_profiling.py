# import pandas as pd
# from matplotlib import pyplot as plt
# import numpy as np

# # Load orders data
# orders = pd.read_csv("data/raw/olist_orders_dataset.csv")


# # ============================================================
# # 1. DATASET OVERVIEW
# # ============================================================

# print("=== DATASET OVERVIEW ===")
# print("Number of rows:", len(orders))
# print("Number of columns:", len(orders.columns))

# # ============================================================
# # 2. COLUMNS
# # ============================================================

# print("\n=== COLUMNS ===")
# print(orders.columns.tolist())

# # ============================================================
# # 3. DATA TYPES
# # ============================================================

# print("\n=== DATA TYPES ===")
# print(orders.dtypes)

# # ============================================================
# # 4. MISSING VALUES
# # ============================================================

# print("\n=== MISSING VALUES ===")
# print(orders.isnull().sum())

# # ============================================================
# # 5. DUPLICATES
# # ============================================================

# print("\n=== DUPLICATE ROWS ===")
# print("Duplicate rows:", orders.duplicated().sum())

# # ============================================================
# # 6. ORDER ID CHECK
# # ============================================================

# print("\n=== ORDER ID CHECK ===")
# print("Unique order IDs:", orders["order_id"].nunique())
# print("Total order IDs:", len(orders))

# # ============================================================
# # 7. ORDER STATUS
# # ============================================================

# print("\n=== ORDER STATUS ===")
# print(orders["order_status"].value_counts())

# #=============================================================
# # Delivery Percentage
# # ============================================================

# total_orders = len(orders)
# delivered_orders = (orders["order_status"] == "delivered").sum()
# delivery_percentage = (delivered_orders / total_orders) * 100
# print("Total orders:", total_orders)
# print("Delivered orders:", delivered_orders)
# print("Delivery percentage:", delivery_percentage)

# #=============================================================
# # Date Conversion
# # ============================================================
# orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"] )
# orders["order_purchase_timestamp"] 
# print(orders["order_purchase_timestamp"].dtype)

# #=============================================================
# # Business order by Month
# # ============================================================

# orders["order_month"] = orders["order_purchase_timestamp"].dt.month
# print(orders[["order_purchase_timestamp", "order_month"]].head())
# monthly_orders = orders["order_month"].value_counts().sort_index()
# print(monthly_orders)

# #=============================================================
# # Business order by Year
# # ============================================================

# orders["order_year"]= orders["order_purchase_timestamp"].dt.year
# orders["order_year"].head()
# yearly_orders = orders["order_year"].value_counts().sort_index()
# print(yearly_orders)

# monthly_orders.idxmax()
# monthly_orders.idxmin()

# print("Highest order month:", monthly_orders.idxmax())
# print("Lowest order month:", monthly_orders.idxmin())


# orders["order_year_month"] = orders["order_purchase_timestamp"].dt.to_period("M")
# print(orders[["order_purchase_timestamp", "order_year_month"]].head())

# monthly_orders = orders["order_year_month"].value_counts().sort_index()
# print(monthly_orders)



########## Order Items##########################################

items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
print("Number of Items : ", len(items))
print("Number of Columns : ",len(items.columns))
print("Columns : ",items.columns.tolist())
print("Datatypes : ",items.dtypes)
print("Number of Missing values :\n",items.isnull().sum())
print("Number of Duplicated :\n",items.duplicated().sum())


items.duplicated(subset=["order_id", "order_item_id"]).sum()

print(items[["order_id", "order_item_id", "product_id", "price"]].head(10))


total_sales = items["price"].sum()
print(total_sales)

print(yearly_orders)


merged = pd.merge(
    orders,
    items,
    on="order_id"
)

merged.columns.tolist()
merged.shape

print(merged["order_year"], total_sales)
merged["price"].sum()
yearly_sales = merged.groupby("order_year")["price"].sum()
print(yearly_sales)

merged.columns.tolist()

monthly_sales = merged.groupby("order_year_month")["price"].sum()
print(monthly_sales)


print("Highest Sales Month",monthly_sales.idxmax())
print("Highest Sales Amount",monthly_sales.max())


print("Lowest Sales Month",monthly_sales.idxmin())
print("Lowest Sales Amount",monthly_sales.min())

order_values = merged.groupby("order_id")["price"].sum()
aov = order_values.mean()
print(aov)

merged.columns

yearly_orders = merged.groupby("order_year")["order_id"].nunique()
print(yearly_orders)



order_values = merged.groupby(["order_year", "order_id"])["price"].sum()
yearly_aov = order_values.groupby("order_year").mean()
print(yearly_aov)


customer_sales  =  merged.groupby("customer_id")["price"].sum()
print(customer_sales .mean())

orders_per_customer   =  merged.groupby("customer_id")["order_id"].nunique()
print(orders_per_customer.mean())

#######   Sales by Yearly month   ###########################################

# monthly_sales = merged.groupby("order_year_month")["price"].sum()

# plt.plot(monthly_sales.index.astype(str), monthly_sales)

# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.title("Monthly Sales Trend")

# plt.xticks(rotation=45)
# plt.locator_params(axis="x", nbins=12)
# plt.ticklabel_format(axis="y", style="plain")
# plt.show()


#################################  Order by month #####################################


# monthly_orders = merged.groupby("order_year_month")["order_id"].nunique()
# print(monthly_orders)

# plt.plot(monthly_orders.index.astype(str), monthly_orders)
# plt.xlabel("Month")
# plt.ylabel("Orders")
# plt.title("Monthly Orders Trend")

# plt.xticks(rotation=45)
# plt.locator_params(axis="x", nbins=12)
# plt.ticklabel_format(axis="y", style="plain")
# plt.show()


############### Product/ Category Performance ###########################


############## Category Sales#############################################

products = pd.read_csv("data/raw/olist_products_dataset.csv")

products.shape
products.head()
products.columns.tolist()
products.isnull().sum()
products.duplicated().sum()

product_merged = pd.merge(merged,products, on = "product_id")

print(product_merged.columns.tolist())


category_sales = product_merged.groupby("product_category_name")["price"].sum()
print(category_sales)

top10_category = category_sales.sort_values(ascending=False).head(10)

plt.barh(top10_category.index, top10_category)
plt.xlabel("Sales")
plt.ylabel("Categories")
plt.title("Product Performance")

plt.xticks(rotation=45)
plt.locator_params(axis="x", nbins=12)
plt.ticklabel_format(axis="y", style="plain")
plt.show()


######### Product Sales ################################################


product_sales = product_merged.groupby("product_id")["price"].sum()
print(product_sales)

top10_product = product_sales.sort_values(ascending=False).head(10)

plt.barh(top10_product.index, top10_product)
plt.xlabel("Sales")
plt.ylabel("Products")
plt.title("Product Performance")

plt.xticks(rotation=45)
plt.locator_params(axis="x", nbins=12)
plt.ticklabel_format(axis="y", style="plain")
plt.show()


####################### Sales by CustomerState #################################
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")

customers.head()

customers.shape
orders.columns

customerorders_merged = pd.merge(customers, orders , on = "customer_id")

print(customerorders_merged.columns.tolist())


customer_orders_items_merged = pd.merge(customerorders_merged, items, on = "order_id")

############ State with Most sales ##############

SalesPerformance_byState = customer_orders_items_merged.groupby("customer_state")["price"].sum()
Tope10Sales_byState = SalesPerformance_byState.sort_values(ascending = False).head(10)

plt.bar(Tope10Sales_byState.index, Tope10Sales_byState)
plt.show()


###################### Delivery Performance ###########################

orders[["order_delivered_customer_date","order_estimated_delivery_date"]].head()

order_delivered_customer_date = pd.to_datetime(orders.order_delivered_customer_date)
order_estimated_delivery_date = pd.to_datetime(orders.order_estimated_delivery_date)

delivery_delay_days = order_delivered_customer_date - order_estimated_delivery_date

orders["delivery_delay_days"] = delivery_delay_days.dt.days

print(orders["delivery_delay_days"])


print(
    orders[
        [
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
            "delivery_delay_days"
        ]
    ].head(10)
)

orders["delivery_delay_days"].mean()
orders["delivery_delay_days"].min()
orders["delivery_delay_days"].max()

orders.loc[
    orders["delivery_delay_days"].idxmin(),
    [
        "order_id",
        "order_status",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
        "delivery_delay_days"
    ]
]


orders.loc[
    orders["delivery_delay_days"].idxmax(),
    [
        "order_id",
        "order_status",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
        "delivery_delay_days"
    ]
]

orders["delivery_status"] = np.where(
    orders["delivery_delay_days"] > 0,
    "Late",
    "On Time"
)

status_counts = orders["delivery_status"].value_counts()
late_percentage  = status_counts["Late"] / status_counts.sum() * 100
print(late_percentage )


########### Customer Analytics ###############################################

orders_per_customer = customerorders_merged.groupby("customer_unique_id")["order_id"].nunique()

print(orders_per_customer.head())


customer_type = np.where(
    orders_per_customer == 1,
    "One-time",
    "Repeat"
)
customer_type_counts = pd.Series(customer_type).value_counts()

print(customer_type_counts)

################## Reviews ##############################################
reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")

print(reviews.columns.tolist())

delivery_reviews = pd.merge(
    orders[["order_id", "delivery_status"]],
    reviews[["order_id", "review_score"]],
    on="order_id"
)

review_by_delivery = delivery_reviews.groupby(
    "delivery_status"
)["review_score"].mean()

print(review_by_delivery)

###################### Sql loading #############################

sales_data = pd.read_sql("SELECT * FROM vw_sales", connection)
sales_data.to_csv("data/processed/sales_view.csv", index=False)

sales_data.shape