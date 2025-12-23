import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employees_updated.csv')

plt.bar(df['Name'], df['Salary'])
plt.title("Employee Salaries")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()

plt.figure(figsize=(9, 5))
plt.bar(df['Name'], df['Salary'], color='skyblue')
plt.title("Employee Salaries", fontsize=14)
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()

plt.figure(figsize=(9, 5))
bars = plt.bar(df['Name'], df['Salary'], color='lightgreen')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             height,
             f'{int(height)}',
             ha='center',
             va='bottom')

plt.title("Employee Salaries")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()

plt.figure(figsize=(9, 5))
plt.bar(df['Name'], df['Salary'], color='coral')
plt.xticks(rotation=30)
plt.title("Employee Salaries")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
plt.bar(df['Name'], df['Salary'], color='slateblue')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title("Employee Salaries")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
plt.plot(df['Name'], df['Salary'], marker='o', linewidth=2, label='Original')
plt.plot(df['Name'], df['Salary_Raised'], marker='o', linestyle='--', linewidth=2, label='Raised')

plt.title("Salary Increase Comparison")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
