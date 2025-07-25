# 🟢 STEP 1: Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🟢 STEP 2: Creating a Hand-Made Business Dataset

data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Product': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B'],
    'Quarter': ['Q1', 'Q1', 'Q2', 'Q2', 'Q3', 'Q3', 'Q4', 'Q4', 'Q1', 'Q2'],
    'Sales': [12000, 15000, 10000, 11000, 17000, 9000, 13000, 14500, 12500, 15500],
    'Profit': [3000, 4000, 2000, 2500, 5000, 1500, 3500, 3800, 3200, 4100],
    'Discount': [0.05, 0.1, 0.02, 0.07, 0.03, 0.08, 0.04, 0.06, 0.05, 0.09],
    'Customer_Rating': [4, 5, 3, 4, 5, 2, 4, 5, 3, 5]
}

df = pd.DataFrame(data)
print(df)

# ===================================================================================
# 🔵 MATPLOTLIB: Top 10 Visualizations + When to Use
# ===================================================================================

plt.figure(figsize=(18, 40))
plt.subplots_adjust(hspace=0.6)

# 1️⃣ Bar Chart – Total Sales by Region
plt.subplot(10, 1, 1)
df.groupby('Region')['Sales'].sum().plot(kind='bar', color='orange')
plt.title("1. Bar Chart: Total Sales by Region")
# 🟢 Why: Use to compare discrete categories (e.g., regions)

# 2️⃣ Line Chart – Sales Trend for Product A
plt.subplot(10, 1, 2)
df[df['Product'] == 'A'].plot(x='Quarter', y='Sales', kind='line', marker='o', ax=plt.gca())
plt.title("2. Line Chart: Sales Trend for Product A")
# 🟢 Why: Great for visualizing trends over time

# 3️⃣ Pie Chart – Product Sales Share
plt.subplot(10, 1, 3)
df.groupby('Product')['Sales'].sum().plot.pie(autopct='%1.1f%%', ax=plt.gca())
plt.title("3. Pie Chart: Product Sales Share")
# 🟢 Why: Use to show proportion of whole

# 4️⃣ Histogram – Profit Distribution
plt.subplot(10, 1, 4)
df['Profit'].plot(kind='hist', bins=5, color='green', edgecolor='black')
plt.title("4. Histogram: Profit Distribution")
# 🟢 Why: Understand data distribution

# 5️⃣ Scatter Plot – Sales vs Profit
plt.subplot(10, 1, 5)
plt.scatter(df['Sales'], df['Profit'], color='red')
plt.title("5. Scatter Plot: Sales vs Profit")
# 🟢 Why: Check relationships between two numeric variables

# 6️⃣ Box Plot – Profit by Product
plt.subplot(10, 1, 6)
df.boxplot(column='Profit', by='Product', ax=plt.gca())
plt.title("6. Box Plot: Profit by Product")
plt.suptitle('')
# 🟢 Why: See distribution and outliers

# 7️⃣ Area Chart – Sales over Time
plt.subplot(10, 1, 7)
df.sort_values(by='Quarter').groupby('Quarter')['Sales'].sum().plot(kind='area', alpha=0.4)
plt.title("7. Area Chart: Quarterly Sales")
# 🟢 Why: Visualize trends and volume

# 8️⃣ Stacked Bar Chart – Sales by Region & Product
plt.subplot(10, 1, 8)
df_pivot = df.pivot_table(index='Region', columns='Product', values='Sales', aggfunc='sum')
df_pivot.plot(kind='bar', stacked=True, ax=plt.gca())
plt.title("8. Stacked Bar: Sales by Region & Product")
# 🟢 Why: Shows category contribution within total

# 9️⃣ Horizontal Bar – Average Profit by Product
plt.subplot(10, 1, 9)
df.groupby('Product')['Profit'].mean().plot(kind='barh', color='purple')
plt.title("9. Horizontal Bar: Avg Profit by Product")
# 🟢 Why: Better visual when category names are long

# 🔟 Custom Marker Plot – Rating vs Discount
plt.subplot(10, 1, 10)
plt.plot(df['Customer_Rating'], df['Discount'], 'g^')
plt.title("10. Custom Marker Plot: Rating vs Discount")
# 🟢 Why: Use for stylish categorical markers

plt.tight_layout()
plt.show()

# ===================================================================================
# 🔵 SEABORN: Top 10 Visualization with Explanation
# ===================================================================================

plt.figure(figsize=(18, 40))
plt.subplots_adjust(hspace=0.6)

# 1️⃣ Barplot – Profit by Product
plt.subplot(10, 1, 1)
sns.barplot(data=df, x='Product', y='Profit', palette='Blues')
plt.title("1. Barplot: Profit by Product")
# 🟢 Why: Elegant category comparison

# 2️⃣ Countplot – Product Distribution
plt.subplot(10, 1, 2)
sns.countplot(data=df, x='Product', palette='Set2')
plt.title("2. Countplot: Product Occurrence")
# 🟢 Why: Frequency of each category

# 3️⃣ Lineplot – Sales Trend
plt.subplot(10, 1, 3)
sns.lineplot(data=df, x='Quarter', y='Sales', hue='Product')
plt.title("3. Lineplot: Sales Trend per Product")
# 🟢 Why: Multi-series trend view

# 4️⃣ Histogram – Profit
plt.subplot(10, 1, 4)
sns.histplot(data=df, x='Profit', kde=True, color='green')
plt.title("4. Histogram with KDE: Profit")
# 🟢 Why: Understand data shape

# 5️⃣ Boxplot – Sales by Region
plt.subplot(10, 1, 5)
sns.boxplot(data=df, x='Region', y='Sales', palette='pastel')
plt.title("5. Boxplot: Sales by Region")
# 🟢 Why: Outlier and distribution

# 6️⃣ Violinplot – Rating by Product
plt.subplot(10, 1, 6)
sns.violinplot(data=df, x='Product', y='Customer_Rating', palette='muted')
plt.title("6. Violinplot: Rating Spread")
# 🟢 Why: Distribution + Density

# 7️⃣ Scatterplot – Sales vs Profit
plt.subplot(10, 1, 7)
sns.scatterplot(data=df, x='Sales', y='Profit', hue='Product', style='Region')
plt.title("7. Scatterplot: Sales vs Profit")
# 🟢 Why: Relationship between two values

# 8️⃣ Heatmap – Correlation Matrix
plt.subplot(10, 1, 8)
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("8. Heatmap: Numeric Correlation")
# 🟢 Why: Understand relationships

# 9️⃣ Swarmplot – Discount per Region
plt.subplot(10, 1, 9)
sns.swarmplot(data=df, x='Region', y='Discount', hue='Product')
plt.title("9. Swarmplot: Discount Patterns")
# 🟢 Why: Distribution + individual points

# 🔟 Pairplot – All Variables
plt.subplot(10, 1, 10)
sns.pairplot(df, hue='Product')
plt.title("10. Pairplot: Multi-Variable Plot")
# 🟢 Why: Overview of all pairwise relationships

plt.tight_layout()
plt.show()