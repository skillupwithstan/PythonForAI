import pandas as pd

df = pd.read_csv('data.csv')

# Verify what the data looks like BEFORE cleaning
print("--- BEFORE CLEANING ---")
print(df.head())  # Prints the first 5 rows

# Double-check missing value counts
print("\n--- MISSING VALUE COUNT PER COLUMN ---")
print(df.isna().sum())
#print(df.isna().stack()[lambda x: x].index)
print(df.isna().any(axis=1))

# Run your cleaning code
df = df.drop_duplicates()
df['Age'] = df['Age'].fillna(0)
df['Department'] = df['Department'].fillna('Unknown')

# Verify changes AFTER cleaning
print("\n--- AFTER CLEANING ---")
print(df.head())

# Double-check missing value counts
print("\n--- MISSING VALUE COUNT PER COLUMN ---")
print(df.isna().sum())