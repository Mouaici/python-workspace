import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employees.csv')
print(df)

# Convert Salary column to NumPy array
salaries = df['Salary'].to_numpy()

# Calculate statistics
mean_salary = np.mean(salaries)
max_salary = np.max(salaries)
min_salary = np.min(salaries)

print("Mean salary:", mean_salary)
print("Max salary:", max_salary)
print("Min salary:", min_salary)

df['Salary_Raised'] = np.round(df['Salary'] * 1.10, 2)
print(df)

dept_avg = df.groupby('Department')['Salary'].mean()
print(dept_avg)

plt.figure(figsize=(7, 5))
plt.bar(dept_avg.index, dept_avg.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(df['Name'], df['Salary'], marker='o', label='Original')
plt.plot(df['Name'], df['Salary_Raised'], marker='o', label='Raised')
plt.title("Salary Increase per Employee")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()

df.to_csv('employees_final.csv', index=False)
