import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('employees_updated.csv')

# Fix floating-point artifacts
df['Salary_Raised'] = df['Salary_Raised'].round(2)

print(df)

avg_salary = np.mean(df['Salary'])
max_salary = np.max(df['Salary'])
min_salary = np.min(df['Salary'])

print("Average salary:", avg_salary)
print("Max salary:", max_salary)
print("Min salary:", min_salary)

# Average salary per department
dept_avg = df.groupby('Department')['Salary'].mean()
print(dept_avg)

fig, axes = plt.subplots(2, 1, figsize=(8, 10))

# Bar chart
axes[0].bar(df['Name'], df['Salary'])
axes[0].set_title("Employee Salaries")
axes[0].set_ylabel("Salary")
axes[0].tick_params(axis='x', rotation=30)

# Line chart
axes[1].plot(df['Name'], df['Salary_Raised'], marker='o')
axes[1].set_title("Salary After Raise")
axes[1].set_ylabel("Salary")
axes[1].tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.show()
