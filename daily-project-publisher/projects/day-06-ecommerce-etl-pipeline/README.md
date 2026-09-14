# Day 6: E-Commerce Multi-Table Relational ETL (Star Schema)

## Overview
This project implements a multi-source relational ETL pipeline for an e-commerce platform. It ingests data across four relational entities (`Customers`, `Products`, `Orders`, and `Payments`), applies data cleaning/normalization (email lowercasing & trimming), filters settled transactions (`COMPLETED`), computes line-item total gross amounts, and loads the transformed dataset into a Star Schema SQLite database (`ecommerce_warehouse.db`).

## Star Schema Architecture
- **Dimension Tables:** `dim_customers`, `dim_products`
- **Fact Table:** `fact_orders` (`order_id`, `customer_id`, `product_id`, `quantity`, `gross_amount`, `order_date`)

## Usage
Run the ETL script:
```bash
python ecommerce_etl.py
```
