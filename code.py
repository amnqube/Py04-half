# =========================
# Setup: Import and Sample DataFrame
# Creates a DataFrame called df1 for testing all methods
# =========================

import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Eve', 'Frank', 'Bob'],
    'Score': [85, 67, 90, 85, 67, 77, 67],
    'Grade': ['B', 'C', 'A', 'B', 'C', 'B', 'C']
}
df1 = pd.DataFrame(data)
print("# df1:")
print(df1)

# =========================
# Creating a Conditional Column from More Than 2 Choices - np.select()
# Adds a column 'Performance' based on Score
# =========================

conditions = [
    df1['Score'] >= 85,
    (df1['Score'] >= 70) & (df1['Score'] < 85),
    df1['Score'] < 70
]
choices = ['Excellent', 'Good', 'Poor']
df1['Performance'] = np.select(conditions, choices, default='Unknown')

print("\n# df1 after adding 'Performance' column:")
print(df1)

# =========================
# The isin() Method
# Filters rows where Score is 67 or 85
# =========================

df_filtered = df1[df1['Score'].isin([67, 85])]
print("\n# Rows where Score is 67 or 85:")
print(df_filtered)

# =========================
# Find Duplicate Rows with the .duplicated() Method
# Finds full row duplicates and Name duplicates
# =========================

# Full row duplicates
duplicates = df1[df1.duplicated()]
print("\n# Full duplicate rows:")
print(duplicates)

# Duplicate names
duplicate_names = df1[df1.duplicated(subset='Name')]
print("\n# Duplicate Name rows (not first occurrence):")
print(duplicate_names)

# =========================
# Drop Duplicate Elements with the .drop_duplicates() Method
# Removes full duplicate rows or duplicates based on a column
# =========================

# Remove full duplicate rows
df_no_duplicates = df1.drop_duplicates()
print("\n# DataFrame with full duplicates removed:")
print(df_no_duplicates)

# Remove duplicates based on 'Name' only, keep first
df_no_name_duplicates = df1.drop_duplicates(subset='Name', keep='first')
print("\n# DataFrame with duplicate Names removed (keep first):")
print(df_no_name_duplicates)

# =========================
# Get and Count Unique Values - .unique() and .nunique()
# Lists and counts unique values in 'Score' column
# =========================

unique_scores = df1['Score'].unique()
print("\n# Unique scores:")
print(unique_scores)

unique_score_count = df1['Score'].nunique()
print("\n# Number of unique scores:")
print(unique_score_count)