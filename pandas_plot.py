import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv('employees_updated.csv')
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Salary'])
plt.title("Employee Salaries")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['Salary'])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

dept_counts = df['Department'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Employees per Department")
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(df['Name'], df['Salary'], marker='o', label='Original Salary')
plt.plot(df['Name'], df['Salary_Raised'], marker='o', label='Raised Salary')
plt.title("Salary Increase")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()

