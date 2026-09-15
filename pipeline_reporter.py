import os
import sqlite3
import pandas as pd
from datetime import datetime

def create_sample_data():
    os.makedirs("data", exist_ok=True)
    raw_data = pd.DataFrame({
        "transaction_id": [1001, 1002, 1003, 1004, 1005, 1001],
        "category": ["Electronics", "Clothing", "Electronics", "Home", "Clothing", "Electronics"],
        "region": ["North", "South", "North", "West", "South", "North"],
        "amount": [12000.0, None, 4500.0, 3200.0, 1500.0, 12000.0],
        "discount_pct": [0.10, 0.05, 0.15, 0.00, 0.20, 0.10]
    })
    raw_data.to_csv("data/raw_sales_stream.csv", index=False)

def run_end_to_end_pipeline():
    create_sample_data()

    # 1. Extraction
    df = pd.read_csv("data/raw_sales_stream.csv")

    # 2. Cleaning & Imputation
    df = df.drop_duplicates().reset_index(drop=True)
    df["amount"] = df["amount"].fillna(df.groupby("category")["amount"].transform("mean"))
    df["net_revenue"] = df["amount"] * (1 - df["discount_pct"])

    # 3. SQL Database Storage
    conn = sqlite3.connect("production_analytics.db")
    df.to_sql("clean_sales", conn, if_exists="replace", index=False)

    # 4. KPI Analytics Query
    summary = pd.read_sql("""
        SELECT
            region,
            COUNT(transaction_id) as total_orders,
            ROUND(SUM(net_revenue), 2) as net_revenue,
            ROUND(AVG(net_revenue), 2) as average_order_value
        FROM clean_sales
        GROUP BY region
        ORDER BY net_revenue DESC;
    """, conn)
    conn.close()

    # 5. Automated Executive Report Generation
    report = f"""# Executive KPI Analytics Report
*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

## Regional Performance
{summary.to_markdown(index=False)}

## Summary
- Total Transactions: {len(df)}
- Net Revenue: ₹{df['net_revenue'].sum():,.2f}
"""
    with open("executive_summary_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    print("Executive Report successfully generated.")

if __name__ == "__main__":
    run_end_to_end_pipeline()
