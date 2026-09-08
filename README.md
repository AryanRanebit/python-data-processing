# 📊 Day 1: Pandas Data Preprocessing, Deduplication & Normalization

## 📌 Problem Overview & Objective
This project demonstrates foundational data engineering and data preprocessing techniques using **Python** and **Pandas**. In production pipelines, raw data frequently contains missing values (`NaN`), duplicate rows, and features measured across disparate scales. This assignment establishes automated routines to cleanse, deduplicate, and normalize raw tabular data.

---

## ⚙️ Key Techniques & Mathematical Foundations

### 1. Missing Value Imputation
- **Numerical Features (`Age`, `Marks`)**: Mean imputation replacing `NaN` with $\mu = \frac{1}{N}\sum_{i=1}^N x_i$.
- **Categorical Features (`Name`)**: Constant value imputation (`'Unknown'`).

### 2. Deduplication
- Identification and removal of duplicate tuple entries using full-row hashing via `df.drop_duplicates()`.

### 3. Min-Max Feature Normalization
Rescales features into a standard bounded range $[0, 1]$:

$$X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$$

---

## 🚀 Execution & Usage

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Preprocessing Pipeline
```bash
python data_preprocessing.py
```

---

## 📈 Sample Results & Output

### Original Raw Dataset
| Name | Age | Marks |
| :--- | :--- | :--- |
| Amit | 22.0 | 85.0 |
| Riya | 24.0 | 90.0 |
| Amit | 22.0 | 85.0 |
| Neha | NaN | 78.0 |
| NaN | 26.0 | NaN |

### Final Cleaned & Normalized Dataset
| Name | Age | Marks | Age_Normalized | Marks_Normalized |
| :--- | :--- | :--- | :--- | :--- |
| Amit | 22.0 | 85.0 | 0.000 | 0.583 |
| Riya | 24.0 | 90.0 | 0.500 | 1.000 |
| Neha | 23.5 | 78.0 | 0.375 | 0.000 |
| Unknown | 26.0 | 84.5 | 1.000 | 0.542 |

---
*Created as part of the Automated 7-Day College Data Engineering Series.*
