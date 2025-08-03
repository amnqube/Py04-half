# 📌 Step 1: Import necessary libraries
import seaborn as sns                 # 🎨 Seaborn is a statistical data visualization library built on top of matplotlib
import matplotlib.pyplot as plt       # 📊 Matplotlib is used by Seaborn underneath to render the visualizations
import pandas as pd                   # 📋 Pandas for working with tabular data (DataFrames)
import numpy as np                    # 🔢 Numpy for numerical operations and random number generation

# 📌 Step 2: Create a custom fruit dataset with 10 different fruits and numerical features
np.random.seed(42)  # 🔁 Ensures reproducibility of random numbers (so your output is same every time)

# 🧺 Sample fruit names
fruits = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange', 'Pineapple', 'Guava', 'Papaya', 'Kiwi', 'Peach']

# 🧮 Assign random values to each fruit for various features
df = pd.DataFrame({
    'Fruit': fruits,                                          # 🏷️ Category column
    'Sweetness': np.random.randint(60, 100, size=10),         # 🍬 How sweet the fruit is (out of 100)
    'Water_Content': np.random.randint(60, 95, size=10),      # 💧 Water percentage
    'Weight': np.random.randint(100, 500, size=10),           # ⚖️ Grams
    'Shelf_Life': np.random.randint(5, 20, size=10)           # 📆 Days before spoiling
})

# 🖍 Define custom color palette for each fruit (makes charts colorful and distinguishable)
fruit_colors = dict(zip(fruits, sns.color_palette("tab10", 10)))  
# 🟦 "tab10" gives 10 distinct, visually pleasant colors

# --------------------------------------------------------
# 📊 1. Barplot — Show average sweetness
plt.figure(figsize=(10, 5))  # 📏 Set figure size
sns.barplot(x='Fruit', y='Sweetness', data=df, palette=fruit_colors)  
# 🎯 Barplot compares values across categories
# 🔸 x='Fruit': Category axis
# 🔸 y='Sweetness': Height of bars
# 🔸 palette=fruit_colors: Apply unique color per fruit
plt.title('Sweetness of Different Fruits')  # 📝 Title of chart
plt.xticks(rotation=45)  # 🔄 Rotate x labels to prevent overlap
plt.tight_layout()  # 🧼 Avoids label cutoff
plt.show()

# --------------------------------------------------------
# 📊 2. Countplot — Frequency of each fruit (needs repeated values)
plt.figure(figsize=(10, 5))
sns.countplot(x='Fruit', data=df.loc[df.index.repeat(2)], palette=fruit_colors)
# 🔁 We repeat rows to simulate frequency since each fruit appears once
# 🔸 countplot: used for showing count of categorical variable
plt.title('Fruit Count (Simulated Frequency)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------------------------------------------------------
# 📊 3. Boxplot — Visualize distribution + outliers of weight
plt.figure(figsize=(8, 5))
sns.boxplot(x='Fruit', y='Weight', data=df, palette=fruit_colors)
# 📦 Box shows median, quartiles, and outliers
# 🔸 Outliers are dots outside the whiskers
plt.title('Fruit Weight Distribution')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------------------------------------------------------
# 📊 4. Violinplot — Same as boxplot but with distribution curve
plt.figure(figsize=(8, 5))
sns.violinplot(x='Fruit', y='Weight', data=df, palette=fruit_colors)
# 🎻 Adds density estimation over the box
# 🔸 Good for understanding shape of distribution
plt.title('Weight Distribution (Violin Plot)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------------------------------------------------------
# 📊 5. Stripplot — Individual dots for each observation
plt.figure(figsize=(8, 5))
sns.stripplot(x='Fruit', y='Shelf_Life', data=df, palette=fruit_colors, size=10, jitter=True)
# 🔘 Shows all data points as dots
# 🔸 size=10: Increases dot size
# 🔸 jitter=True: Spreads dots sideways for visibility
plt.title('Shelf Life of Fruits')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------------------------------------------------------
# 📊 6. Swarmplot — Like stripplot but auto-adjusts to avoid overlap
plt.figure(figsize=(8, 5))
sns.swarmplot(x='Fruit', y='Sweetness', data=df, palette=fruit_colors, size=10)
# 🐝 Better dot layout — no overlap
plt.title('Sweetness Spread (Swarmplot)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------------------------------------------------------
# 📊 7. Heatmap — Visualize correlation matrix
corr = df.drop(columns=['Fruit']).corr()  # 🧮 Compute correlation between numeric features
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='YlGnBu', linewidths=0.5)
# 🔥 Heatmap shows pairwise correlation
# 🔸 annot=True: Show actual values in cells
# 🔸 cmap='YlGnBu': Yellow-Green-Blue color scheme
# 🔸 linewidths=0.5: Thin lines between boxes
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.show()

# --------------------------------------------------------
# 📊 8. Pairplot — Show pairwise scatter plots + histograms
sns.pairplot(df.drop(columns=['Fruit']), corner=True)
# 🔷 Automatically creates scatter plots for every pair of numeric variables
# 🔸 corner=True: Show only lower triangle (avoids duplicates)
plt.suptitle('Pairwise Feature Comparison', y=1.02)  # 🏷 Title on top
plt.tight_layout()
plt.show()

# --------------------------------------------------------
# 📊 9. Scatterplot — Water vs Sweetness
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Water_Content', y='Sweetness', data=df, hue='Fruit', palette=fruit_colors, s=100)
# 🔸 hue='Fruit': Color by fruit
# 🔸 s=100: Size of dots
plt.title('Water Content vs Sweetness')
plt.tight_layout()
plt.show()

# --------------------------------------------------------
# 📊 10. Lineplot — Line showing shelf life
plt.figure(figsize=(10, 5))
sns.lineplot(x='Fruit', y='Shelf_Life', data=df, marker='o', color='teal', linewidth=2)
# 📈 Lineplot for trends
# 🔸 marker='o': Adds circle markers
# 🔸 linewidth=2: Thicker line for visibility
plt.title('Shelf Life of Fruits (Line Chart)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()