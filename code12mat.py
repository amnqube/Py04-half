# 📌 Step 1: Import required libraries

import matplotlib.pyplot as plt     # 📚 Core visualization library in Python for 2D charts
import pandas as pd                 # 📚 Used for handling and analyzing tabular data like Excel sheets
import numpy as np                  # 🔢 Used for numerical operations (arrays, random numbers, math functions)

# 📌 Step 2: Create dataset — 10 fruits and their sales/returns across different channels
data = {
    'Fruit': ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange', 'Pineapple', 'Guava', 'Papaya', 'Kiwi', 'Peach'],
    'Offline_Sales': [120, 150, 90, 100, 110, 130, 80, 95, 70, 105],   # 🛒 Sales in physical stores
    'Online_Sales': [100, 130, 85, 90, 105, 120, 75, 85, 65, 95],      # 📦 Sales through online platforms
    'Returns': [10, 12, 5, 7, 8, 10, 4, 6, 3, 5]                        # 🔁 Number of returned items
}

# 📌 Step 3: Convert the dictionary into a DataFrame for easier plotting and manipulation
df = pd.DataFrame(data)  # 🧾 Now each column can be accessed easily like df['Offline_Sales']

# 📌 Step 4: Define color map — to keep consistent colors across all charts
color_map = {
    'Offline_Sales': 'royalblue',   # 🔵 Chosen for visual calm and clarity
    'Online_Sales': 'seagreen',     # 🟢 Symbolizes success/progress
    'Returns': 'salmon'             # 🔴 Often used for alerts, warnings, or negative values
}

# ===========================================================
# 📊 1. LINE PLOT
plt.figure(figsize=(10, 5))  # 📏 Size of canvas in inches (width=10, height=5)

# 📈 Plot a line chart — 'Fruit' on x-axis, 'Offline_Sales' on y-axis
plt.plot(df['Fruit'],                      # x-axis: Fruit names (categorical)
         df['Offline_Sales'],              # y-axis: Offline sales
         color=color_map['Offline_Sales'], # 🟦 Consistent color
         marker='o',                        # ⚪ Add circles at data points
         linestyle='-')                     # ➖ Solid line between points

plt.title('Offline Fruit Sales (Line Plot)')     # 📝 Main title at top
plt.xlabel('Fruit Name')                         # ↔ Label for x-axis
plt.ylabel('Number of Units Sold')               # ↕ Label for y-axis
plt.grid(True)                                   # 🔲 Adds grid for better readability
plt.legend(['Offline Sales'])                    # 🧭 Legend shows what line means (label)
plt.tight_layout()                               # ✅ Adjust spacing to avoid overlap/cutoff
plt.show()                                       # 🎯 Display chart

# ===========================================================
# 📊 2. VERTICAL BAR CHART
plt.figure(figsize=(10, 5))
plt.bar(df['Fruit'], df['Offline_Sales'], color=color_map['Offline_Sales'])  # 📊 Bars for offline sales
plt.title('Offline Fruit Sales (Bar Plot)')
plt.xlabel('Fruit Name')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)  # 🔄 Rotate x-axis labels for better visibility if names are long
plt.grid(axis='y')       # 📐 Add horizontal lines only (not vertical)
plt.tight_layout()
plt.show()

# ===========================================================
# 📊 3. HORIZONTAL BAR CHART
plt.figure(figsize=(10, 5))
plt.barh(df['Fruit'], df['Offline_Sales'], color=color_map['Offline_Sales'])  # 📊 Horizontal version
plt.title('Offline Fruit Sales (Horizontal Bar)')
plt.xlabel('Units Sold')    # ↔ Now horizontal
plt.ylabel('Fruit')         # ↕ Now vertical
plt.tight_layout()
plt.show()

# ===========================================================
# 📊 4. PIE CHART
plt.figure(figsize=(8, 8))  # ⭕ Square for symmetric pie
plt.pie(df['Offline_Sales'],               # 🔢 Values to plot
        labels=df['Fruit'],                # 🏷 Slice names
        autopct='%1.1f%%',                 # 💯 Show percentage up to 1 decimal
        startangle=90)                     # 🔄 Start from top (default is 0°)
plt.title('Sales Distribution by Fruit (Pie Chart)')
plt.tight_layout()
plt.show()

# ===========================================================
# 📊 5. BOX PLOT
plt.figure(figsize=(6, 5))
plt.boxplot(df['Offline_Sales'])          # 📦 Shows spread, quartiles, outliers
plt.title('Sales Spread (Box Plot)')
plt.ylabel('Offline Sales')
plt.grid(True)                            # 🔳 Helps in visualizing medians, IQR
plt.tight_layout()
plt.show()

# ===========================================================
# 📊 6. HISTOGRAM
plt.figure(figsize=(7, 5))
plt.hist(df['Offline_Sales'],             # 🧮 Raw values to group
         bins=5,                           # 📊 Number of bins (ranges like 60-80, 80-100 etc.)
         color=color_map['Offline_Sales'],# 🎨 Fill color
         edgecolor='black')               # ⚫ Border around bars
plt.title('Offline Sales Distribution (Histogram)')
plt.xlabel('Sales Range')                 # 🏷 Intervals of values
plt.ylabel('Frequency')                   # 🔢 How many data points per interval
plt.grid(True)
plt.tight_layout()
plt.show()

# ===========================================================
# 📊 7. STACKED BAR CHART
plt.figure(figsize=(10, 5))
plt.bar(df['Fruit'], df['Offline_Sales'], label='Offline', color=color_map['Offline_Sales'])  # 🧱 Base
plt.bar(df['Fruit'], df['Returns'], bottom=df['Offline_Sales'], label='Returns', color=color_map['Returns'])  
# 📌 `bottom` stacks returns on top of offline sales
plt.title('Sales vs Returns (Stacked Bar)')
plt.xlabel('Fruit Name')
plt.ylabel('Total Units')
plt.legend()                  # 📘 Label each color block
plt.tight_layout()
plt.show()

# ===========================================================
# 📊 8. GROUPED BAR CHART
bar_width = 0.35                                  # 🧱 Width of each bar
x = np.arange(len(df['Fruit']))                  # 🔢 X-axis values as numbers [0, 1, 2, ...]
plt.figure(figsize=(10, 5))
plt.bar(x, df['Offline_Sales'], width=bar_width, label='Offline', color=color_map['Offline_Sales'])  # 🟦 First group
plt.bar(x + bar_width, df['Online_Sales'], width=bar_width, label='Online', color=color_map['Online_Sales'])  
# 🟩 Second group, slightly shifted
plt.xlabel('Fruit Name')
plt.ylabel('Units Sold')
plt.title('Offline vs Online Sales (Grouped Bar)')
plt.xticks(x + bar_width / 2, df['Fruit'], rotation=45)  # 🔁 Center labels between the 2 bars
plt.legend()
plt.tight_layout()
plt.show()

# ===========================================================
# 📊 9. SCATTER PLOT
plt.figure(figsize=(10, 5))
plt.scatter(df['Offline_Sales'],           # 🔢 X-axis: offline sales
            df['Online_Sales'],            # 🔢 Y-axis: online sales
            color='purple',                # 💜 Color of dots
            s=100)                         # ⚪ Size of dots (s = size)
plt.title('Offline vs Online Sales (Scatter Plot)')
plt.xlabel('Offline Sales')
plt.ylabel('Online Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# ===========================================================
# 📊 10. AREA CHART
plt.figure(figsize=(10, 5))
x = np.arange(len(df['Fruit']))         # 🔢 Numerical positions for each fruit
y = df['Offline_Sales'].values          # 📊 Convert Series to array for fill_between

plt.plot(x, y,                          # 🔗 Draw line chart first
         color=color_map['Offline_Sales'],
         label='Offline Sales')         # 🏷 Label for legend

plt.fill_between(x, y, color=color_map['Offline_Sales'], alpha=0.3)  
# 🟧 Fill area under line | alpha=0.3 makes it semi-transparent (0=invisible, 1=solid)

plt.xticks(x, df['Fruit'], rotation=45)  # 🔢 Replace 0,1,2 with actual fruit names
plt.title('Offline Sales Trend (Area Chart)')
plt.xlabel('Fruit')
plt.ylabel('Units Sold')
plt.legend()
plt.tight_layout()
plt.show()