import pandas as pd

# Create a Series of stock prices
prices = pd.Series([150.25, 152.10, 149.80, 155.00])

print(prices)

# 1. Create dummy data
raw_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Bob'],
    'Age': [25, 30, None, 22, 30],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'IT'],
    'Salary': [50000, 70000, 65000, 48000, 70000]
}

# 2. Convert to a DataFrame
df = pd.DataFrame(raw_data)

# 3. Save it as data.csv
df.to_csv('data.csv', index=False)
#df.to_excel('data1.xlsx', index=False)
print("File 'data.csv' created successfully!")

# Load data from a CSV file
df = pd.read_csv('data.csv')

print(df.head())       # Displays the first 5 rows of the dataset
print(df.tail())       # Displays the last 5 rows of the dataset
print(df.info())       # Shows column data types, memory usage, and non-null counts
print(df.describe())   # Provides summary statistics (mean, min, max) for numeric columns
print(df.shape)        # Returns a tuple representing (rows, columns)
