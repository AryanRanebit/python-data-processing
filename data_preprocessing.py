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

# Save processed output
df.to_csv("processed_students.csv", index=False)
print("\nProcessed data exported to 'processed_students.csv'")
