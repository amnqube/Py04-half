# =========================
# 🟢 Setup: Import and Sample DataFrame
# Create df1 for testing all tasks
# =========================

import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [85, 67, 90, 76, 92],
    'Grade': ['B', 'C', 'A', 'B', 'A']
}
df1 = pd.DataFrame(data)
print("# df1:")
print(df1)
#       Name  Score Grade
# 0    Alice     85     B
# 1      Bob     67     C
# 2  Charlie     90     A
# 3    David     76     B
# 4      Eve     92     A

# =========================
# 🟢 First Look at the Dataset, Setting Index, and Selecting Columns
# View top rows, set custom index, select specific columns
# =========================

print("\n# Head of df1:")
print(df1.head())
#       Name  Score Grade
# 0    Alice     85     B
# 1      Bob     67     C
# 2  Charlie     90     A
# 3    David     76     B
# 4      Eve     92     A

df1.set_index('Name', inplace=True)
print("\n# df1 with 'Name' set as index:")
print(df1)
#         Score Grade
# Name                
# Alice      85     B
# Bob        67     C
# Charlie    90     A
# David      76     B
# Eve        92     A

print("\n# Selecting 'Score' column:")
print(df1['Score'])
# Name
# Alice      85
# Bob        67
# Charlie    90
# David      76
# Eve        92
# Name: Score, dtype: int64

# =========================
# 🟢 Selecting elements by index label with .loc
# Use row and column names
# =========================

print("\n# .loc to select Score of 'Charlie':")
print(df1.loc['Charlie', 'Score'])
# 90

print("\n# .loc to select multiple rows:")
print(df1.loc[['Bob', 'Eve']])
#         Score Grade
# Name                
# Bob        67     C
# Eve        92     A

# =========================
# 🟢 Selecting elements by index position with .iloc
# Use row/column numbers (starts at 0)
# =========================

print("\n# .iloc to get 2nd row, 1st column (Score of Bob):")
print(df1.iloc[1, 0])
# 67

print("\n# .iloc to get first 3 rows:")
print(df1.iloc[0:3])
#         Score Grade
# Name                
# Alice      85     B
# Bob        67     C
# Charlie    90     A

# =========================
# 🟢 Set New Value for a Cell in a DataFrame
# Update a value using .loc
# =========================

df1.loc['Bob', 'Score'] = 75
print("\n# Updated Bob's Score to 75:")
print(df1)
#         Score Grade
# Name                
# Alice      85     B
# Bob        75     C
# Charlie    90     A
# David      76     B
# Eve        92     A

# =========================
# 🟢 Drop Rows or Columns from a DataFrame
# Drop by label or position
# =========================

df_dropped_row = df1.drop('David')
print("\n# Dropped row 'David':")
print(df_dropped_row)
#         Score Grade
# Name                
# Alice      85     B
# Bob        75     C
# Charlie    90     A
# Eve        92     A

df_dropped_col = df1.drop(columns='Grade')
print("\n# Dropped column 'Grade':")
print(df_dropped_col)
#         Score
# Name         
# Alice      85
# Bob        75
# Charlie    90
# David      76
# Eve        92

# =========================
# 🟢 Create Random Sample with the sample() Method
# Get random subset of rows
# =========================

df_sample = df1.sample(n=2, random_state=1)
print("\n# Random sample of 2 rows:")
print(df_sample)
#         Score Grade
# Name                
# Charlie    90     A
# Alice      85     B

# =========================
# 🟢 Filter a DataFrame with the query() Method
# Use condition strings (like SQL)
# =========================

df_filtered = df1.query("Score > 80")
print("\n# Students with Score > 80:")
print(df_filtered)
#         Score Grade
# Name                
# Alice      85     B
# Charlie    90     A
# Eve        92     A

# =========================
# 🟢 The apply() Method
# Apply function to each row or column
# =========================

def add_bonus(score):
    return score + 5

df1['Bonus'] = df1['Score'].apply(add_bonus)
print("\n# Apply: Added 5 bonus to Score:")
print(df1)
#         Score Grade  Bonus
# Name                      
# Alice      85     B     90
# Bob        75     C     80
# Charlie    90     A     95
# David      76     B     81
# Eve        92     A     97

# =========================
# 🟢 Lambda Function + apply()
# One-liner to double the score
# =========================

df1['DoubleScore'] = df1['Score'].apply(lambda x: x * 2)
print("\n# Lambda + apply: Double Score:")
print(df1)
#         Score Grade  Bonus  DoubleScore
# Name                                    
# Alice      85     B     90          170
# Bob        75     C     80          150
# Charlie    90     A     95          180
# David      76     B     81          152
# Eve        92     A     97          184

# =========================
# 🟢 Make a Copy of a DataFrame with copy()
# Create independent copy to avoid changing original
# =========================

df_copy = df1.copy()
df_copy['Copied'] = True
print("\n# Copied df1 to df_copy and added 'Copied' column:")
print(df_copy)
#         Score Grade  Bonus  DoubleScore  Copied
# Name                                          
# Alice      85     B     90          170    True
# Bob        75     C     80          150    True
# Charlie    90     A     95          180    True
# David      76     B     81          152    True
# Eve        92     A     97          184    True

print("\n# Original df1 unchanged:")
print(df1)
#         Score Grade  Bonus  DoubleScore
# Name                                    
# Alice      85     B     90          170
# Bob        75     C     80          150
# Charlie    90     A     95          180
# David      76     B     81          152
# Eve        92     A     97          184