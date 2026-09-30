CREATE VIEW vw_sales AS
SELECT
    oi.order_id,
    oi.order_item_id,
    oi.product_id,
    oi.seller_id,
    oi.price,
    oi.freight_value,
    o.customer_id,
    o.order_status,
    o.order_purchase_timestamp,
    c.customer_unique_id,
    c.customer_state,
    p.product_category_name
FROM fact_order_items oi
JOIN dim_orders o
    ON oi.order_id = o.order_id
JOIN dim_customers c
    ON o.customer_id = c.customer_id
JOIN dim_products p
    ON oi.product_id = p.product_id;