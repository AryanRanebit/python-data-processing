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


if __name__ == "__main__":
    init_database()

    batch1_data = {
        "id": [1, 2, 3, 4],
        "customer_name": ["Alice", "Bob", "CorruptedUser", "Diana"],
        "account_balance": [1500.50, -50.00, 2300.00, 500.00],
        "credit_score": [750, 680, 200, 810],
        "updated_at": ["2026-09-01T10:00:00", "2026-09-01T10:05:00", "2026-09-01T10:10:00", "2026-09-01T10:15:00"]
    }
    pd.DataFrame(batch1_data).to_csv("batch1_input.csv", index=False)
    print("--- Running Pipeline on Batch 1 ---")
    run_pipeline("batch1_input.csv")

    batch2_data = {
        "id": [5, 6],
        "customer_name": ["Evan", "Fiona"],
        "account_balance": [3200.00, 1800.00],
        "credit_score": [720, 790],
        "updated_at": ["2026-09-02T11:00:00", "2026-09-02T11:30:00"]
    }
    pd.DataFrame(batch2_data).to_csv("batch2_input.csv", index=False)
    print("\n--- Running Pipeline on Batch 2 (Incremental Delta Load) ---")
    run_pipeline("batch2_input.csv")
