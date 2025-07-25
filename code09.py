# 🟢 Import pandas
import pandas as pd

# 🟢 Create larger DataFrames with 4 columns each
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Amit', 'Bina', 'Chetan'],
    'Age': [23, 25, 24],
    'City': ['Delhi', 'Mumbai', 'Pune']
})

df2 = pd.DataFrame({
    'ID': [4, 5, 6],
    'Name': ['Divya', 'Eshan', 'Farah'],
    'Age': [26, 27, 28],
    'City': ['Jaipur', 'Kolkata', 'Chennai']
})

df3 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Salary': [50000, 60000, 70000],
    'Experience': [2, 3, 4],
    'Department': ['IT', 'HR', 'Sales']
})

# 🟢 1. Vertical Concatenation (same columns stacked together)
pd.concat([df1, df2], ignore_index=True)

# Output:
#    ID   Name  Age     City
# 0   1   Amit   23    Delhi
# 1   2   Bina   25   Mumbai
# 2   3 Chetan   24     Pune
# 3   4  Divya   26   Jaipur
# 4   5  Eshan   27  Kolkata
# 5   6  Farah   28  Chennai

# 🟢 2. Horizontal Concatenation (combine side-by-side)
pd.concat([df1, df2], axis=1)

# Output:
#    ID   Name  Age    City  ID   Name  Age     City
# 0   1   Amit   23   Delhi   4  Divya   26   Jaipur
# 1   2   Bina   25  Mumbai   5  Eshan   27  Kolkata
# 2   3 Chetan   24    Pune   6  Farah   28  Chennai

# 🟢 3. Outer Join (combine everything)
pd.merge(df1, df3, on='ID', how='outer')

# Output:
#    ID   Name   Age     City   Salary  Experience Department
# 0   1   Amit  23.0    Delhi      NaN         NaN        NaN
# 1   2   Bina  25.0   Mumbai  50000.0         2.0         IT
# 2   3 Chetan  24.0     Pune  60000.0         3.0         HR
# 3   4  Divya  26.0   Jaipur  70000.0         4.0      Sales

# 🟢 4. Inner Join (only matching IDs from both)
pd.merge(df1, df3, on='ID', how='inner')

# Output:
#    ID   Name  Age   City  Salary  Experience Department
# 0   2   Bina   25 Mumbai   50000           2         IT
# 1   3 Chetan   24   Pune   60000           3         HR

# 🟢 5. Left Join (all rows from df1)
pd.merge(df1, df3, on='ID', how='left')

# Output:
#    ID   Name  Age    City   Salary  Experience Department
# 0   1   Amit   23   Delhi      NaN         NaN        NaN
# 1   2   Bina   25  Mumbai  50000.0         2.0         IT
# 2   3 Chetan   24   Pune  60000.0         3.0         HR

# 🟢 6. Right Join (all rows from df3)
pd.merge(df1, df3, on='ID', how='right')

# Output:
#    ID   Name   Age   City  Salary  Experience Department
# 0   2   Bina  25.0 Mumbai   50000           2         IT
# 1   3 Chetan  24.0   Pune   60000           3         HR
# 2   4    NaN   NaN    NaN   70000           4      Sales