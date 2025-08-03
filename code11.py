# 📌 Step 1: Import necessary libraries
import pandas as pd         # For data manipulation
import numpy as np          # For numerical operations

# 📌 Step 2: Create and save the sample dataset as xyz1.csv
# This simulates the real-world CSV with slightly dirty and varied data
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', None],  # Note the None (missing value)
    'category': ['A', 'B', 'A', 'B', 'A', 'A', 'B', 'A'],
    'sales': [100, 200, 150, 180, 120, 130, 220, 110],
    'region': ['East', 'West', 'East', 'West', 'East', 'West', 'East', 'East'],
    'tags': ['promo,new', 'featured', 'promo', 'promo,old', 'new', '', 'featured,promo', 'promo'],
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
             '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08'],
    'score': [90, 80, 70, None, 60, 75, 85, 55]
}

df = pd.DataFrame(data)                  # Create DataFrame
df.to_csv('xyz1.csv', index=False)       # Save to CSV
print("✅ Dataset saved as xyz1.csv")    # Confirm save

# Output:
# ✅ Dataset saved as xyz1.csv

# 📌 Step 3: Load the dataset from saved file
df = pd.read_csv('xyz1.csv')            # Load data into DataFrame

# Convert 'date' column to datetime for time-series operations later
df['date'] = pd.to_datetime(df['date'])

# ───────────────────────────────────────────────────────────────
# ✅ 1. MultiIndex using groupby
# Grouping by 'region' and 'category' to get total sales
grouped = df.groupby(['region', 'category'])[['sales']].sum()  # Creates hierarchical index
print("\n🔹 1. MultiIndex Grouped Result:\n", grouped)

# Output:
# 🔹 1. MultiIndex Grouped Result:
#                 sales
# region category       
# East   A           480
#        B           220
# West   A           130
#        B           380

# ───────────────────────────────────────────────────────────────
# ✅ 2. explode()
# First convert 'tags' string to list so explode() works
df['tags'] = df['tags'].str.split(',')  # Convert to list: 'promo,new' → ['promo', 'new']
df_exploded = df.explode('tags')        # One row per tag
print("\n🔹 2. After explode():\n", df_exploded[['name', 'tags']].head(6))

# Output:
# 🔹 2. After explode():
#      name      tags
# 0   Alice     promo
# 0   Alice       new
# 1     Bob   featured
# 2  Charlie     promo
# 3   David     promo
# 3   David       old

# ───────────────────────────────────────────────────────────────
# ✅ 3. melt()
# Reshape from wide to long format
df_melted = pd.melt(df, id_vars=['id', 'name'], value_vars=['sales', 'score'],
                    var_name='metric', value_name='value')
print("\n🔹 3. Melted Data:\n", df_melted.head(6))

# Output:
# 🔹 3. Melted Data:
#    id     name metric  value
# 0   1    Alice  sales  100.0
# 1   2      Bob  sales  200.0
# 2   3  Charlie  sales  150.0
# 3   4    David  sales  180.0
# 4   5      Eva  sales  120.0
# 5   6    Frank  sales  130.0

# ───────────────────────────────────────────────────────────────
# ✅ 4. .query()
df_query = df.query("sales > 100 and region == 'East'")  # Easy readable filter
print("\n🔹 4. Filtered using query():\n", df_query[['name', 'sales', 'region']])

# Output:
# 🔹 4. Filtered using query():
#      name  sales region
# 2  Charlie    150   East
# 5    Frank    130   West
# 6    Grace    220   East
# 7     None    110   East

# ───────────────────────────────────────────────────────────────
# ✅ 5. map() and replace()
df['region_code'] = df['region'].map({'East': 'E', 'West': 'W'})  # map: clean replacement
df['category'] = df['category'].replace({'A': 'Alpha', 'B': 'Beta'})  # replace: safer general version
print("\n🔹 5. After map() and replace():\n", df[['region', 'region_code', 'category']].head())

# Output:
# 🔹 5. After map() and replace():
#   region region_code category
# 0   East           E   Alpha
# 1   West           W    Beta
# 2   East           E   Alpha
# 3   West           W    Beta
# 4   East           E   Alpha

# ───────────────────────────────────────────────────────────────
# ✅ 6. Time-Series resample and rolling
df.set_index('date', inplace=True)          # Set datetime as index

# Weekly total sales
weekly_sales = df['sales'].resample('W').sum()
print("\n🔹 6. Weekly Sales:\n", weekly_sales)

# Output:
# 🔹 6. Weekly Sales:
# date
# 2023-01-01    100
# 2023-01-08   1110
# Freq: W-SUN, Name: sales, dtype: int64

# Rolling 3-day average of score
rolling_score = df['score'].rolling(3).mean()
print("\n🔹 6. Rolling Score (3-day avg):\n", rolling_score.head(6))

# Output:
# 🔹 6. Rolling Score (3-day avg):
# date
# 2023-01-01          NaN
# 2023-01-02          NaN
# 2023-01-03    80.000000
# 2023-01-04    75.000000
# 2023-01-05    65.000000
# 2023-01-06    67.500000
# Name: score, dtype: float64

df.reset_index(inplace=True)  # Reset index back to default for next steps

# ───────────────────────────────────────────────────────────────
# ✅ 7. Handling Missing Values
print("\n🔹 7. Missing values per column:\n", df.isnull().sum())

# Fill score with mean
df['score'] = df['score'].fillna(df['score'].mean())

# Drop rows with missing name
df = df.dropna(subset=['name'])

# Output:
# 🔹 7. Missing values per column:
# id             0
# name           1
# category       0
# sales          0
# region         0
# tags           0
# date           0
# score          1
# region_code    0
# dtype: int64

# ───────────────────────────────────────────────────────────────
# ✅ 8. pipe()
def lowercase_columns(df):
    df.columns = [col.lower() for col in df.columns]  # Lowercase all column names
    return df

df = df.pipe(lowercase_columns)
print("\n🔹 8. Columns after pipe():\n", df.columns.tolist())

# Output:
# 🔹 8. Columns after pipe():
# ['id', 'name', 'category', 'sales', 'region', 'tags', 'date', 'score', 'region_code']

# ───────────────────────────────────────────────────────────────
# ✅ 9. Memory Optimization with downcast
print("\n🔹 9. Before downcast:\n", df.dtypes)

df['sales'] = pd.to_numeric(df['sales'], downcast='integer')
df['score'] = pd.to_numeric(df['score'], downcast='float')

print("\n🔹 9. After downcast:\n", df.dtypes)

# Output:
# 🔹 9. Before downcast:
# id                      int64
# name                   object
# category               object
# sales                   int64
# region                 object
# tags                   object
# date           datetime64[ns]
# score                 float64
# region_code            object
# dtype: object

# 🔹 9. After downcast:
# id                      int64
# name                   object
# category               object
# sales                   int16
# region                 object
# tags                   object
# date           datetime64[ns]
# score                 float32
# region_code            object
# dtype: object


