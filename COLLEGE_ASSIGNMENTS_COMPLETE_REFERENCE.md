# 🎓 College Data Engineering & Preprocessing Assignment Suite
## Complete Project Reference & Automated GitHub Publishing Guide

This document contains **the exact problem statements, raw code snippets, sample datasets, and objectives** provided for the college lab assignments, along with the automated setup instructions so anyone with **Antigravity** can generate, test, and schedule them on GitHub.

---

# Table of Contents
1. [Prerequisites & 1-Minute GitHub Setup](#-step-1-prerequisites--github-cli-setup)
2. [Master Antigravity Autonomous Prompt](#-step-2-master-prompt-for-antigravity)
3. [Exact Project Specifications, Raw Code & Topics](#-exact-project-specifications--code)
   - [Project 1: Pandas Data Preprocessing, Deduplication & Normalization](#project-1-pandas-data-preprocessing-deduplication--normalization)
   - [Project 2: Noise Elimination, Feature Selection & EDA](#project-2-noise-elimination-feature-selection--eda)
   - [Project 3: Extracting Data from APIs and Flat Files (ETL Pipeline)](#project-3-extracting-data-from-apis-and-flat-files-etl-pipeline)
   - [Project 4: Setting up Apache Airflow and Creating a DAG](#project-4-setting-up-apache-airflow-and-creating-a-dag)
   - [Project 5: Data Validation, Quarantine & Incremental Loading](#project-5-data-validation-quarantine--incremental-loading)
   - [Project 6: E-Commerce Multi-Table Relational ETL (Star Schema)](#project-6-e-commerce-multi-table-relational-etl-star-schema)
   - [Project 7: End-to-End Pipeline (CSV → Cleaning → SQL DB → Report)](#project-7-end-to-end-pipeline-csv--cleaning--sql-db--report)
4. [Bonus: Authentic Green Contribution Heatmap Prompt](#-step-3-bonus-authentic-github-green-graph-generator)

---

# 🚀 Step 1: Prerequisites & GitHub CLI Setup

Before running the automated prompt in Antigravity, authenticate your GitHub account on your computer:

```bash
gh auth login
```

**Select these options when prompted:**
- Account: **GitHub.com**
- Preferred protocol: **HTTPS**
- Authenticate Git with GitHub credentials? **Yes**
- Authentication method: **Login with a web browser**
- Press `Enter`, copy the 8-character device code, paste it into the browser window that opens, and click **Authorize**.

---

# 📋 Step 2: Master Prompt for Antigravity

Copy and paste this exact prompt into a new chat in **Antigravity**:

```text
I have 7 college projects in Data Preprocessing and Data Engineering that I need to upload to my GitHub. I want an automated 100% cloud-based Daily Project Publisher using GitHub Actions that uploads 1 complete project every morning at 9:00 AM IST to my GitHub profile, even if my laptop is closed or turned off.

Here is what you need to do:

1. Check my authenticated GitHub account using `gh auth status` and `gh api user`.
2. Create an orchestration workspace directory named `daily-project-publisher`.
3. Scaffold all 7 project folders inside `projects/` using the exact code, datasets, and objectives below. Each project must have:
   - Complete, runnable, tested Python scripts (0 errors).
   - Sample CSV input data and outputs.
   - A comprehensive README.md with problem overview, mathematical formulas, and output tables.
   - `requirements.txt` and `.gitignore`.

4. The 7 Projects to build:
   - Day 1: `pandas-data-preprocessing` (Missing value mean/constant imputation, deduplication, Min-Max feature normalization).
   - Day 2: `eda-outlier-feature-selection` (IQR outlier elimination, VarianceThreshold feature selection, EDA histograms and boxplots).
   - Day 3: `api-csv-etl-pipeline` (REST API data ingestion via requests, JSON flattening with pd.json_normalize, flat CSV merge on ID, warehouse staging).
   - Day 4: `airflow-etl-orchestration` (Apache Airflow Directed Acyclic Graph with EmptyOperator anchor, BashOperator extraction, and success metrics logger).
   - Day 5: `data-validation-incremental-etl` (Pre-load data quality validation, corrupt record quarantine log, timestamp watermark incremental delta loading into SQLite).
   - Day 6: `ecommerce-etl-pipeline` (Multi-source relational ETL: Customers, Orders, Products, Payments with Star Schema dimensional modeling in SQLite).
   - Day 7: `end-to-end-data-pipeline-reporting` (End-to-end pipeline: CSV Ingestion -> Pandas Cleaning -> SQLite Relational DB -> Automated Markdown KPI Report).

5. Create the autonomous publishing engine `publish_next.py` and state manifest `projects_manifest.json` tracking Days 1 through 7.
6. Create the GitHub Actions workflow `.github/workflows/daily_publisher.yml`:
   - Scheduled cron: '30 3 * * *' (03:30 UTC = 09:00 AM IST daily).
   - Manual trigger: workflow_dispatch.
   - Executes `python publish_next.py` with GH_TOKEN: ${{ secrets.PUBLISHER_TOKEN }}.
   - Commits and pushes the updated manifest back to the repository.

7. Initialize git, create a private repository named `daily-project-publisher` on my GitHub account, and push the codebase.
8. Configure the secret `PUBLISHER_TOKEN` using `gh secret set PUBLISHER_TOKEN -b "$(gh auth token)" --repo <username>/daily-project-publisher`.
9. Immediately publish Day 1 (`pandas-data-preprocessing`) right now as a public repository so my first assignment is live today. Days 2 through 7 will follow automatically every morning at 9:00 AM IST on cloud autopilot!
```

---

# 📦 Exact Project Specifications & Code

Here is the exact code, topics, and problem statements for all 7 projects:

---

### Project 1: Pandas Data Preprocessing, Deduplication & Normalization

#### Objective:
Python program using Pandas to handle missing values, duplicate records, and data normalization.

#### Exact Code:
```python
import pandas as pd

# Sample Data
data = {
    'Name': ['Amit', 'Riya', 'Amit', 'Neha', None],
    'Age': [22, 24, 22, None, 26],
    'Marks': [85, 90, 85, 78, None]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# -----------------------------
# 1. Handling Missing Values
# -----------------------------
print("\nHandling Missing Values...")

# Fill missing Age with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Marks with mean
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Fill missing Name with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')

print(df)

# -----------------------------
# 2. Removing Duplicate Rows
# -----------------------------
print("\nRemoving Duplicates...")

df = df.drop_duplicates()

print(df)

# -----------------------------
# 3. Data Normalization (Min-Max)
# Formula: (x - min) / (max - min)
# -----------------------------
print("\nNormalizing Age and Marks...")

df['Age_Normalized'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

df['Marks_Normalized'] = (df['Marks'] - df['Marks'].min()) / (df['Marks'].max() - df['Marks'].min())

print(df)

# Final Data
print("\nFinal Processed Data:")
print(df)
```

---

### Project 2: Noise Elimination, Feature Selection & EDA

#### Objective:
Python program demonstrating Noise Elimination (outlier removal via IQR), Feature Selection (removing constant or low-variance features), and Exploratory Data Analysis (EDA) using Pandas, NumPy, Matplotlib, and Scikit-learn.

#### Exact Code:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold

# -----------------------------
# Sample Dataset
# -----------------------------
data = {
    'Age': [20, 21, 22, 23, 24, 100],   # 100 is an outlier (noise)
    'Marks': [75, 80, 85, 90, 95, 20],
    'Attendance': [85, 88, 90, 92, 94, 50],
    'Constant': [1, 1, 1, 1, 1, 1]      # Constant feature
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# =====================================
# 1. Noise Elimination (Outlier Removal)
# =====================================
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[(df['Age'] >= lower) & (df['Age'] <= upper)]

print("\nDataset after Noise Elimination:")
print(df_clean)

# =====================================
# 2. Feature Selection
# Remove constant or low-variance features
# =====================================
selector = VarianceThreshold(threshold=0.0)
selected = selector.fit_transform(df_clean)

selected_columns = df_clean.columns[selector.get_support()]

print("\nSelected Features:")
print(selected_columns)

# =====================================
# 3. Exploratory Data Analysis (EDA)
# =====================================

print("\nDataset Information:")
print(df_clean.info())

print("\nStatistical Summary:")
print(df_clean.describe())

print("\nCorrelation Matrix:")
print(df_clean.corr())

# Histogram
df_clean.hist(figsize=(8,6))
plt.suptitle("Histogram of Features")
plt.savefig("eda_histogram.png")
plt.show()

# Boxplot
df_clean.boxplot(figsize=(8,5))
plt.title("Boxplot of Dataset")
plt.savefig("eda_boxplot.png")
plt.show()
```

---

### Project 3: Extracting Data from APIs and Flat Files (ETL Pipeline)

#### Objective:
Write a Python script to fetch user data from a public REST API, clean it, and merge it with a flat CSV file containing location details.

#### Exact Code:
```python
import pandas as pd
import requests


def extract_api_data(url):
    """Fetches data from a REST API and returns a DataFrame."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Normalizing JSON data into a flat table
        return pd.json_normalize(data)
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return pd.DataFrame()


def extract_csv_data(file_path):
    """Reads a flat CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError as e:
        print(f"File Error: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    # 1. API Extraction (JSONPlaceholder)
    api_url = "https://jsonplaceholder.typicode.com/users"
    api_df = extract_api_data(api_url)
    
    if not api_df.empty:
        target_cols = [c for c in ["id", "name", "email", "company.name"] if c in api_df.columns]
        api_df = api_df[target_cols]
        if "company.name" in api_df.columns:
            api_df.rename(columns={"company.name": "company"}, inplace=True)

    # 2. Flat File Extraction (Mock CSV Data)
    csv_file = "locations.csv"

    # Creating a sample file for testing
    pd.DataFrame({
        "id": list(range(1, 11)),
        "city": [
            "New York", "London", "Paris", "Tokyo", "Berlin",
            "Delhi", "Sydney", "Moscow", "Cairo", "Beijing"
        ],
        "country": [
            "USA", "UK", "France", "Japan", "Germany",
            "India", "Australia", "Russia", "Egypt", "China"
        ]
    }).to_csv(csv_file, index=False)

    csv_df = extract_csv_data(csv_file)

    # 3. Data Transformation & Merging
    if not api_df.empty and not csv_df.empty:
        merged_df = pd.merge(api_df, csv_df, on="id", how="inner")
        print("\n--- Merged ETL Pipeline Data View ---")
        print(merged_df.head())

        # Save to target Data Lake / Warehouse stage
        output_file = "cleaned_warehouse_profiles.csv"
        merged_df.to_csv(output_file, index=False)
        print(f"\nData successfully saved to '{output_file}'")
```

---

### Project 4: Setting up Apache Airflow and Creating a DAG

#### Objective:
Configure a Directed Acyclic Graph (DAG) in Apache Airflow to run daily, executing sequential dependency tasks: a start notifier (`EmptyOperator`), an extraction script (`BashOperator`), and a pipeline success logger (`BashOperator`).

#### Exact Code (`dags/data_pipeline_dag.py`):
```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

# Default arguments for workflow execution
default_args = {
    "owner": "data_engineering_lab",
    "depends_on_past": False,
    "start_date": datetime(2026, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG context
with DAG(
    "university_etl_orchestration",
    default_args=default_args,
    description="Lab assignment for API and Flat File ETL orchestration",
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=["etl", "orchestration"]
) as dag:

    # Task 1: Pipeline Init Anchor
    start_pipeline = EmptyOperator(task_id="start_pipeline")

    # Task 2: Run Python Extraction Script
    execute_extraction = BashOperator(
        task_id="run_extraction_script",
        bash_command="python3 scripts/data_extraction.py",
    )

    # Task 3: Finalize and Log Metrics
    pipeline_complete = BashOperator(
        task_id="log_pipeline_success",
        bash_command='echo "ETL Execution completed successfully at $(date)"',
    )

    # Linear Dependency Chain
    start_pipeline >> execute_extraction >> pipeline_complete
```

---

### Project 5: Data Validation, Quarantine & Incremental Loading

#### Objectives:
- Design an ETL process to identify and remove invalid records.
- Create a pipeline that performs data validation before loading data into the target database.
- Implement incremental data loading instead of loading the entire dataset every time.

#### Complete Implementation (`etl_validator.py`):
```python
import os
import sqlite3
import pandas as pd

DB_FILE = "warehouse.db"
QUARANTINE_FILE = "quarantine_invalid_records.csv"

def init_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_metrics (
            id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            account_balance REAL NOT NULL,
            credit_score INTEGER NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS etl_watermark (
            pipeline_name TEXT PRIMARY KEY,
            last_processed_timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_watermark():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT last_processed_timestamp FROM etl_watermark WHERE pipeline_name = 'customer_etl'")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else "1970-01-01T00:00:00"

def update_watermark(ts):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO etl_watermark (pipeline_name, last_processed_timestamp)
        VALUES ('customer_etl', ?)
        ON CONFLICT(pipeline_name) DO UPDATE SET last_processed_timestamp=excluded.last_processed_timestamp
    """, (ts,))
    conn.commit()
    conn.close()

def validate_data(df):
    # Rule 1: ID & Name not null
    # Rule 2: account_balance >= 0
    # Rule 3: 300 <= credit_score <= 850
    valid_mask = (
        df['id'].notnull() &
        df['customer_name'].notnull() &
        (df['account_balance'] >= 0.0) &
        (df['credit_score'] >= 300) & (df['credit_score'] <= 850)
    )
    return df[valid_mask].copy(), df[~valid_mask].copy()

def run_pipeline(csv_batch):
    raw_df = pd.read_csv(csv_batch)
    valid_df, invalid_df = validate_data(raw_df)

    if not invalid_df.empty:
        print(f"Quarantined {len(invalid_df)} invalid record(s).")
        invalid_df.to_csv(QUARANTINE_FILE, mode='a', index=False, header=not os.path.exists(QUARANTINE_FILE))

    watermark = get_watermark()
    delta_df = valid_df[valid_df['updated_at'] > watermark]

    if not delta_df.empty:
        conn = sqlite3.connect(DB_FILE)
        delta_df.to_sql("customer_metrics", conn, if_exists="append", index=False)
        conn.close()
        update_watermark(delta_df['updated_at'].max())
        print(f"Incrementally loaded {len(delta_df)} new record(s).")
    else:
        print("No new records to load.")
```

---

### Project 6: E-Commerce Multi-Table Relational ETL (Star Schema)

#### Objective:
Build an ETL pipeline for an e-commerce dataset containing customers, orders, products, and payments into a Star Schema relational database.

#### Complete Implementation (`ecommerce_etl.py`):
```python
import sqlite3
import pandas as pd

def run_ecommerce_etl():
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
```

---

### Project 7: End-to-End Pipeline (CSV → Cleaning → SQL DB → Report)

#### Objective:
Build an end-to-end data pipeline: CSV → Python/Pandas → Data Cleaning → SQL Database → Automated Report. Handles both historical and newly arriving data.

#### Complete Implementation (`pipeline_reporter.py`):
```python
import sqlite3
import pandas as pd
from datetime import datetime

def run_end_to_end_pipeline():
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
    with open("executive_summary_report.md", "w") as f:
        f.write(report)
    print("Executive Report successfully generated.")
```

---

# 🎨 Step 3: Bonus Authentic GitHub Green Graph Generator

If your friend wants their GitHub contribution graph to have natural, varied shades of green across the last 10 months (400–500 commits):

```text
Create a public repository named `developer-notes` on my GitHub account.
Write a script that generates ~400 to 500 authentic-looking commits spread realistically across the last 10 months up to today:
- Vary between 1 and 4 commits per day (different shades of green).
- Higher activity on weekdays (~80%), lighter on weekends (~40%), with occasional natural rest days.
- Realistic developer hours (between 10 AM and 10 PM).
- Each commit must add genuine technical notes or algorithms (Swift, Python, Linux, SQL, Git tips) with clear commit messages like "docs(python): add list comprehension tip", "feat(algo): implement binary search".
- Push the repo to my GitHub. (Do not leave any generator script in the repository).
```
