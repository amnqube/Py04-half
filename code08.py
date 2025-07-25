# 🟢 Creating a Sample Dataset
import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen'],
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance', 'IT', 'HR'],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F'],
    'Salary': [50000, 52000, 60000, 58000, 62000, 61000, 63000, 51000],
    'Bonus': [2000, 2500, 3000, 2800, 4000, 3500, 4100, 2300]
}

df = pd.DataFrame(data)

# 🟢 Display the Dataset
print(df)

# 🟢 1. Group by single column and calculate mean
print(df.groupby('Department')['Salary'].mean())
# Output: Average salary for HR, IT, Finance

# 🟢 2. Group by and apply multiple aggregate functions
print(df.groupby('Department')['Salary'].agg(['mean', 'max', 'min']))
# Output: Department-wise mean, max, and min salary

# 🟢 3. Aggregation on multiple columns
print(df.groupby('Department')[['Salary', 'Bonus']].agg({'Salary': 'mean', 'Bonus': 'sum'}))
# Output: Department-wise average salary and total bonus

# 🟢 4. Group by multiple columns (Department + Gender)
print(df.groupby(['Department', 'Gender'])['Salary'].mean())
# Output: Multi-index showing average salary per department and gender

# 🟢 5. Reset index after groupby
print(df.groupby('Department')['Salary'].mean().reset_index())
# Output: Flattened DataFrame with Department, Salary

# 🟢 6. Sort grouped values
print(df.groupby('Department')['Salary'].mean().sort_values(ascending=False))
# Output: Sorted average salaries

# 🟢 7. Count of employees in each department
print(df.groupby('Department').size())
# Output: Number of employees in each department

# 🟢 8. Named Aggregation
print(df.groupby('Department').agg(Avg_Sal=('Salary', 'mean'), Total_Bonus=('Bonus', 'sum')))
# Output: Custom column names for aggregates

# 🟢 9. Filter groups (Departments with avg salary > 55000)
print(df.groupby('Department').filter(lambda x: x['Salary'].mean() > 55000))
# Output: Only rows from departments where avg salary > 55K

# 🟢 10. Transform for broadcasting mean to original df
df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')
print(df)
# Output: New column with department's average salary per row

# 🟢 11. Apply custom logic after groupby (e.g., z-score)
df['Z_Score_Salary'] = df.groupby('Department')['Salary'].apply(lambda x: (x - x.mean()) / x.std())
print(df)
# Output: New column with z-scores of salary within each department

# 🟢 12. Descriptive stats using describe + groupby
print(df.groupby('Department')['Salary'].describe())
# Output: count, mean, std, min, 25%, 50%, 75%, max for each department