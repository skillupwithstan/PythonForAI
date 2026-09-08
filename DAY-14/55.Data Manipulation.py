import pandas as pd

# Sample dataset
df = pd.read_csv('data.csv')
#pd.DataFrame({
#    'Employee': ['Alex', 'Blake', 'Charlie', 'Drew', 'Eden'],
#    'Dept': ['IT', 'HR', 'IT', 'Finance', 'HR'],
#    'Salary': [70000, 50000, 80000, 60000, 55000],
#    'Remote': [True, False, True, False, True]
#})

print(df)

print(df[(df['Age'] >= 25)])

'''
# Filter using a single condition
it_staff = df[df['Dept'] == 'IT']
print(it_staff)

# Filter using multiple conditions (use & for AND, | for OR)
# Note: Each condition MUST be wrapped in parentheses
high_earning_remote = df[(df['Salary'] >= 70000) & (df['Remote'] == True)]
print(high_earning_remote)

# Calculate the average salary for each department
avg_salary_by_dept = df.groupby('Dept')['Salary'].mean()
print(avg_salary_by_dept)

# Calculate multiple metrics at once (Mean and Count)
dept_stats = df.groupby('Dept')['Salary'].agg(['mean', 'count'])
print(dept_stats)

# Add a fixed 10% bonus column
df['Bonus'] = df['Salary'] * 0.10

# Calculate total compensation
df['Total_Comp'] = df['Salary'] + df['Bonus']

print(df)
'''