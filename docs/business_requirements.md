# Business Requirements

## Stakeholder

Primary stakeholder: Head of Sales / Commercial Manager

Secondary stakeholders:

* Finance
* Sales management
* Regional managers
* Product management

## Reporting Objective

Provide management with a reliable view of commercial performance that supports weekly and monthly decision-making.

## Core KPIs

### Revenue

Total sales revenue generated during a defined period.

### Gross Profit

Revenue minus product cost.

### Gross Margin

Gross profit divided by revenue.

### Orders

Number of completed orders.

### Units Sold

Total number of products sold.

### Average Order Value

Revenue divided by number of orders.

### Revenue per Customer

Total revenue divided by unique customers.

## Required Analysis

### Time

* Daily revenue
* Monthly revenue
* Year-over-year growth where sufficient historical data exists
* Monthly gross margin

### Products

* Revenue by product
* Revenue by category
* Gross profit by product
* Gross margin by category
* Best and worst performers

### Geography

* Revenue by German state/region
* Gross margin by region
* Order volume by region

### Customers

* Revenue by customer
* Number of orders per customer
* Average customer order value
* Customer concentration

## Management Questions

The final dashboard and report should allow management to answer:

1. What is happening?
2. Where is it happening?
3. Why might it be happening?
4. Which areas require attention?
5. What actions should management consider?

## Data Quality Requirements

The pipeline should identify:

* Missing values
* Duplicate records
* Invalid dates
* Invalid quantities
* Invalid prices
* Invalid product/customer references
* Impossible revenue values
* Inconsistent categorical values

## Definition of Done

The project is considered complete when:

* Raw data can be processed reproducibly
* Data-quality issues are documented
* Clean data is stored in a structured database
* KPIs can be reproduced using SQL
* Dashboard metrics agree with the analytical layer
* Business insights are documented
* The repository can be understood and reproduced by another developer
