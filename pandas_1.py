import pandas as pd
import numpy as np
# Create a Series from a Python list
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)
s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s)
# Create from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print(df)

print(df['Name'])    # single column
print(df[['Name','Salary']])   # multiple columns
print(df.iloc[0])    # first row by position
print(df.loc[1])     # second row by index

# People with salary > 55000
high_salary = df[df['Salary'] > 55000]
print(high_salary)

print(df['Salary'].mean())    # average salary
print(df['Age'].max())        # oldest age
print(df.describe())          # summary for numeric columns
import pandas as pd

# Read CSV
df = pd.read_csv('employees.csv')

# Show first 5 rows
print(df.head())
print(df.shape)     # rows, columns
print(df.columns)   # column names
print(df.info())    # summary info
# Employees in IT
it_team = df[df['Department'] == 'IT']
print(it_team)

# Employees with Salary > 60000
high_salary = df[df['Salary'] > 60000]
print(high_salary)

# Add a new column: Salary after 10% raise
df['Salary_Raised'] = df['Salary'] * 1.10
print(df)

print(df['Salary'].mean())      # average salary
print(df.groupby('Department')['Salary'].mean())  # avg salary per department
df.to_csv('employees_updated.csv', index=False)
df['Salary_Raised'] = (df['Salary'] * 1.10).round(2)
df['Salary_Raised'] = (df['Salary'] * 1.10).astype(int)
df.to_csv('employees_updated.csv', index=False)

