# 🟢 Import Required Libraries

import pandas as pd
import matplotlib.pyplot as plt

# 🟢 1. Dataset Overview + Making Pivot Table

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Charlie', 'Alice', 'Bob'],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math', 'Science', 'SST', 'SST'],
    'Score': [85, 78, 90, 82, 88, 95, 75, 70]
}
df = pd.DataFrame(data)

print("# Dataset Overview:")
print(df.head())
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())
print("Summary:\n", df.describe())

# Make Pivot Table
pivot_df = df.pivot_table(index='Name', columns='Subject', values='Score', aggfunc='mean')
print("\n# Pivot Table:")
print(pivot_df)

# 🟢 2. Data Visualization with Pandas

# Bar plot: Comparing average scores of students
pivot_df.plot(kind='bar', figsize=(8, 5), title='Average Scores by Student')
plt.xlabel("Name")
plt.ylabel("Average Score")
plt.tight_layout()
plt.grid(True)
plt.show()

# Line plot: Same pivot in line format
pivot_df.plot(kind='line', marker='o', title='Line Plot of Scores')
plt.xlabel("Name")
plt.ylabel("Scores")
plt.tight_layout()
plt.grid(True)
plt.show()

# 🟢 3. Save Plot & Export Pivot Table

# Save bar plot as image
pivot_df.plot(kind='bar', figsize=(8, 5), title='Average Scores by Student')
plt.xlabel("Name")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("average_scores_bar.png")  # 📁 Saved in current directory
plt.close()

# Export pivot table to CSV
pivot_df.to_csv("pivot_table_scores.csv", index=True)  # 📁 Saved in current directory

# 🟢 4. Interactive Visualization with Pandas (basic interactivity using .plot)

# Interactive-like feel (legend, hover enabled in some environments like Jupyter)
pivot_df.plot(title="Interactive-Like Pivot Table View", marker='o')
plt.xlabel("Name")
plt.ylabel("Score")
plt.grid(True)
plt.tight_layout()
plt.show()





# 🟢 Dataset Overview and Making Pivot Table

# df.head() → Shows first 5 rows of the dataset
# df.shape → Tells the (rows, columns) of the dataset
# df.columns.tolist() → Lists all column names
# df.describe() → Summary statistics (mean, std, etc.)
# pd.pivot_table(df, values='col', index='row', columns='col', aggfunc='sum') 
#   → Creates a pivot table from dataframe

# 🟢 Data Visualization with Pandas

# df.plot(kind='bar') 
#   → 'kind' is the type of chart: bar, line, hist, pie, etc.
# df.plot(kind='line', marker='o') 
#   → 'marker' is used to show points (like circles) at data positions
# df.plot(kind='area', alpha=0.6) 
#   → 'alpha' controls transparency (0 = invisible, 1 = fully visible)
# df.plot(kind='bar', color=['red', 'green', 'blue']) 
#   → 'color' sets the color for each series
# df.plot(kind='line', title='Sales Over Time') 
#   → 'title' adds a chart heading
# df.plot(xlabel='Month', ylabel='Sales') 
#   → 'xlabel' and 'ylabel' name the axes
# df.plot(legend=True) 
#   → 'legend=True' adds a legend for clarity
# df.plot(grid=True) 
#   → 'grid=True' adds grid lines for easier reading
# df.plot(figsize=(10, 6)) 
#   → 'figsize' sets the size of the figure in inches (width, height)
# df.plot(rot=45) 
#   → 'rot' rotates x-axis labels for better readability
# df.plot(stacked=True) 
#   → 'stacked=True' stacks values in bar/area plots
# df.plot(subplots=True) 
#   → 'subplots=True' shows each column’s plot in a different subplot

# 🟢 Save Plot and Export Pivot Table

# plt.tight_layout() 
#   → Adjusts spacing so labels/titles don’t overlap
# plt.savefig('filename.png') 
#   → Saves the current plot as an image file
# df.to_csv('pivot.csv', index=True) 
#   → Saves pivot table to a CSV file
# df.to_excel('pivot.xlsx', index=False) 
#   → Saves pivot table to an Excel file

# 🟢 Extra Visual Mastery

# alpha=0.6 
#   → Transparency level in plot elements
# fontsize=12 
#   → Font size for axis labels, ticks, etc.
# color=['blue', 'orange'] 
#   → Set custom colors for bars/lines
# layout='tight' (Used with subplots)
#   → Automatically adjusts layout to prevent overlapping

# 🟢 Interactive Visualization with Pandas

# %matplotlib inline (Jupyter only)
#   → Ensures plots appear in notebook
# %matplotlib widget / notebook 
#   → Enables interactive zoom and hover in notebook
# df.plot(marker='o', figsize=(12, 6), grid=True) 
#   → Combines multiple features for an interactive and clean plot










