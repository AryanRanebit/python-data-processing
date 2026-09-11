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
