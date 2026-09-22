# Data Dictionary

## Purpose

This document will describe the datasets, fields, data types, business meaning, and data-quality considerations used in the Business Performance Intelligence Platform.

## Planned Data Entities

### Orders

Information about customer orders and their lifecycle.

Expected fields may include:

* Order ID
* Customer ID
* Order status
* Purchase timestamp
* Approval timestamp
* Delivery timestamp
* Estimated delivery date

### Customers

Information about customers and their geographic location.

Expected fields may include:

* Customer ID
* Customer unique ID
* Customer ZIP code
* Customer city
* Customer state

### Products

Information about products sold through the marketplace.

Expected fields may include:

* Product ID
* Product category
* Product dimensions
* Product weight

### Order Items

Information about products included in each order.

Expected fields may include:

* Order ID
* Product ID
* Seller ID
* Price
* Freight value

### Payments

Information about payment transactions.

Expected fields may include:

* Order ID
* Payment type
* Payment installments
* Payment value

## Notes

The exact fields, data types, relationships, missing values, and quality issues will be determined during data discovery.

This document will be updated as the dataset is investigated.
