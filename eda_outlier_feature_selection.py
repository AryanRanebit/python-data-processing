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

# Save outputs to CSV for verification
df_clean.to_csv("clean_dataset.csv", index=False)
df_clean[selected_columns].to_csv("selected_features_dataset.csv", index=False)
print("\nCleaned and feature-selected datasets saved.")
