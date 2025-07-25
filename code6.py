# 🟢 Setup: Import Libraries and Create Sample DataFrame
# Added SST as a subject

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Charlie', 'Alice', 'Bob'],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math', 'Science', 'SST', 'SST'],
    'Score': [85, 78, 90, 82, 88, 95, 75, 70]
}
df1 = pd.DataFrame(data)

print("# df1:")
print(df1)

# Output:
#       Name  Subject  Score
# 0    Alice     Math     85
# 1      Bob     Math     78
# 2    Alice  Science     90
# 3      Bob  Science     82
# 4  Charlie     Math     88
# 5  Charlie  Science     95
# 6    Alice      SST     75
# 7      Bob      SST     70

# 🟢 1. pivot(): Rearrange data — Rows = Name, Columns = Subject, Values = Score
# Only works when there's no duplicate (Name+Subject pair)

pivot_df = df1.pivot(index='Name', columns='Subject', values='Score')

print("\n# Pivot table using pivot():")
print(pivot_df)

# Output:
# Subject   Math  SST  Science
# Name                      
# Alice     85.0  75.0     90.0
# Bob       78.0  70.0     82.0
# Charlie   88.0   NaN     95.0

# 🟢 2. pivot_table(): More powerful — handles duplicates using aggregation (mean by default)

pivot_table_df = df1.pivot_table(index='Name', columns='Subject', values='Score', aggfunc='mean')

print("\n# Pivot table using pivot_table():")
print(pivot_table_df)

# Output:
# Subject   Math  SST  Science
# Name                      
# Alice     85.0  75.0     90.0
# Bob       78.0  70.0     82.0
# Charlie   88.0   NaN     95.0

# 🟢 3. Exclude SST from pivot_table(): Filter out SST rows before pivoting

df_no_sst = df1[df1['Subject'] != 'SST']
pivot_excluding_sst = df_no_sst.pivot_table(index='Name', columns='Subject', values='Score', aggfunc='mean')

print("\n# Pivot table excluding SST (using pivot_table()):")
print(pivot_excluding_sst)

# Output:
# Subject   Math  Science
# Name                    
# Alice     85.0     90.0
# Bob       78.0     82.0
# Charlie   88.0     95.0