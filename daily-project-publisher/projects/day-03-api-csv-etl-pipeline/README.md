# 🌐 Day 3: Extracting Data from APIs and Flat Files (ETL Pipeline)

## 📌 Problem Overview & Objective
This assignment demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline in Python:
1. **Extract**: Fetch user details from a public REST API (`JSONPlaceholder`) and read location details from a local flat CSV file.
2. **Transform**: Flatten nested JSON structures using `pandas.json_normalize`, select and rename target attributes, and perform an inner join on user ID.
3. **Load**: Export the unified schema into a staged data warehouse CSV format (`cleaned_warehouse_profiles.csv`).

---

## ⚙️ Key Concepts

### 1. REST API JSON Normalization
$$\text{JSON Response} \xrightarrow{\text{json\_normalize}} \text{Flat Tabular DataFrame}$$

### 2. Relational Inner Join
Merging API user profiles ($D_1$) with location metadata ($D_2$) on key column $\text{id}$:
$$\text{Merged DataFrame} = D_1 \bowtie_{\text{id}} D_2$$

---

## 🚀 Execution & Usage

```bash
pip install -r requirements.txt
python api_csv_etl_pipeline.py
```
