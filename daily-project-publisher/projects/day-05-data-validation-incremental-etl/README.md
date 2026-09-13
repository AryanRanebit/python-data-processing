# 🛡️ Day 5: Data Validation, Quarantine Log & Incremental Watermark Loading

## 📌 Problem Overview & Objective
This assignment implements a production-grade ETL validation and delta-loading pipeline using Python, Pandas, and SQLite:
1. **Pre-Load Data Validation**: Checking records against strict business rules before ingestion.
2. **Quarantine Invalidation**: Isolating corrupted/out-of-bound records into `quarantine_invalid_records.csv`.
3. **High-Watermark Incremental Ingestion**: Tracking timestamp watermarks (`etl_watermark`) to load only new/delta data into `warehouse.db` without full table scans or duplication.

---

## ⚙️ Key Validation & Delta Rules

### 1. Integrity Validation Rules
$$\text{Valid Record} \iff (\text{id} \neq \text{null}) \land (\text{name} \neq \text{null}) \land (\text{balance} \ge 0) \land (300 \le \text{credit\_score} \le 850)$$

### 2. High-Watermark Delta Filter
$$\text{Delta Rows} = \{ r \in \text{Valid Rows} \mid r.\text{updated\_at} > T_{\text{watermark}} \}$$

---

## 🚀 Execution & Usage

```bash
pip install -r requirements.txt
python data_validation_incremental_etl.py
```
