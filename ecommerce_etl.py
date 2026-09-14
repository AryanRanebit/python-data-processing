import os
import sqlite3
import pandas as pd

def create_sample_datasets():
    os.makedirs("data", exist_ok=True)
    
    customers_df = pd.DataFrame({
        "customer_id": [101, 102, 103, 104],
        "name": ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince"],
        "email": ["ALICE@EXAMPLE.COM ", "bob.jones@example.com", "charlie@example.com ", "diana@example.com"]
    })
    customers_df.to_csv("data/customers.csv", index=False)

    products_df = pd.DataFrame({
        "product_id": [201, 202, 203],
        "product_name": ["Laptop", "Smartphone", "Headphones"],
        "price": [1200.0, 800.0, 150.0]
    })
    products_df.to_csv("data/products.csv", index=False)

    orders_df = pd.DataFrame({
        "order_id": [1, 2, 3, 4],
        "customer_id": [101, 102, 101, 103],
        "product_id": [201, 203, 202, 201],
        "quantity": [1, 2, 1, 1],
        "order_date": ["2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04"]
    })
    orders_df.to_csv("data/orders.csv", index=False)

    payments_df = pd.DataFrame({
        "payment_id": [501, 502, 503, 504],
        "order_id": [1, 2, 3, 4],
        "payment_method": ["Credit Card", "PayPal", "Credit Card", "Debit Card"],
        "payment_status": ["COMPLETED", "COMPLETED", "FAILED", "COMPLETED"]
    })
    payments_df.to_csv("data/payments.csv", index=False)

def run_ecommerce_etl():
    create_sample_datasets()

    # Ingest relational entities
    customers = pd.read_csv("data/customers.csv")
    products = pd.read_csv("data/products.csv")
    orders = pd.read_csv("data/orders.csv")
    payments = pd.read_csv("data/payments.csv")

    # Clean & normalize
    customers["email"] = customers["email"].str.lower().str.strip()

    # Filter completed transactions
    settled = payments[payments["payment_status"] == "COMPLETED"]

    # Calculate line totals & join
    fact_orders = orders.merge(products, on="product_id").merge(settled, on="order_id")
    fact_orders["gross_amount"] = fact_orders["quantity"] * fact_orders["price"]

    # Save to SQLite Star Schema
    conn = sqlite3.connect("ecommerce_warehouse.db")
    customers.to_sql("dim_customers", conn, if_exists="replace", index=False)
    products.to_sql("dim_products", conn, if_exists="replace", index=False)
    fact_orders[[
        "order_id", "customer_id", "product_id", "quantity", "gross_amount", "order_date"
    ]].to_sql("fact_orders", conn, if_exists="replace", index=False)
    conn.close()
    print("E-Commerce Star Schema created successfully.")

if __name__ == "__main__":
    run_ecommerce_etl()
