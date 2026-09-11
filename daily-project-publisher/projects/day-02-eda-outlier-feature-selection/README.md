# 📊 Day 2: Noise Elimination, Feature Selection & EDA

## 📌 Problem Overview & Objective
This assignment focuses on data cleaning and feature engineering techniques:
1. **Noise Elimination**: Removing outliers using the Interquartile Range (IQR) method.
2. **Feature Selection**: Identifying and eliminating constant/zero-variance features using Scikit-Learn's `VarianceThreshold`.
3. **Exploratory Data Analysis (EDA)**: Computing statistical summaries, correlation matrices, and distribution visualizations.

---

## ⚙️ Key Concepts

### 1. Interquartile Range (IQR) Outlier Filtering
$$\text{IQR} = Q_3 - Q_1$$
$$\text{Lower Bound} = Q_1 - 1.5 \times \text{IQR}$$
$$\text{Upper Bound} = Q_3 + 1.5 \times \text{IQR}$$

Records outside $[\text{Lower Bound}, \text{Upper Bound}]$ are flagged as noise/outliers and filtered out.

### 2. Variance Threshold Feature Selection
Features with zero variance ($\text{Var}(X) = 0$) provide no explanatory value and are automatically removed from the modeling matrix.

---

## 🚀 Execution & Usage

```bash
pip install -r requirements.txt
python eda_outlier_feature_selection.py
```
