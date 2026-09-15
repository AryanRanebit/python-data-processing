# Day 7: End-to-End Data Pipeline & Executive Reporting

## Overview
This project delivers a complete end-to-end data pipeline in Python & SQLite. It ingests a raw sales stream CSV, cleans duplicates, imputes missing values via category means, calculates net revenue metrics, loads cleaned records into an SQLite analytics database (`production_analytics.db`), and programmatically generates an executive KPI Markdown report (`executive_summary_report.md`).

## Pipeline Workflow
1. **Extraction:** Ingestion of raw streaming transactions from `data/raw_sales_stream.csv`.
2. **Cleaning & Transformation:** Deduplication, missing amount imputation, and net revenue computation.
3. **Storage:** Staging normalized records in `production_analytics.db` (`clean_sales` table).
4. **KPI Analytics & Reporting:** SQL aggregations exported into formatted Markdown reports.

## Usage
Run the pipeline:
```bash
python pipeline_reporter.py
```
