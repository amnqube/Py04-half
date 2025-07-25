import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

#🟢 Load the dataset
df = pd.read_csv('/mnt/data/linear1.csv')
#👉 Reads the CSV file and stores it in a DataFrame called 'df'
#👉 This creates a table with columns like X1, X2, and Y
#👉 Example:
#     X1   X2    Y
#     12   25   105
#     13   27   112

#🟢 Split the data: 70 train, 10 validation, 20 test
train_df = df.iloc[:70]
val_df = df.iloc[70:80]
test_df = df.iloc[80:]
#👉 Splits the dataset into three parts:
#    - Training (first 70 rows): used to teach the model
#    - Validation (next 10 rows): check accuracy while tuning
#    - Test (last 20 rows): final performance check

#🟢 Separate input (X) and output (Y)
X_train = train_df[['X1', 'X2']]
y_train = train_df['Y']

X_val = val_df[['X1', 'X2']]
y_val = val_df['Y']

X_test = test_df[['X1', 'X2']]
y_test = test_df['Y']
#👉 Separates features (X1, X2) and target (Y)
#👉 X_train looks like:
#     X1   X2
#     12   25
#     13   27
#👉 y_train looks like:
#     105
#     112

#🟢 Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
#👉 Fits the model using training data
#👉 It learns the best values for a, b, and c in:
#    Y = a*X1 + b*X2 + c

#🟢 Get the equation of best fit line
intercept = model.intercept_         # This is the constant term (c)
coeff = model.coef_                  # These are coefficients (a and b)
best_fit_eq = f"Y = {coeff[0]:.2f}*X1 + {coeff[1]:.2f}*X2 + {intercept:.2f}"
#👉 Builds the equation using learned values
#👉 Example: if coeff[0]=2.3, coeff[1]=4.5, intercept=10.2
#👉 Then: "Y = 2.30*X1 + 4.50*X2 + 10.20"
#👉 This equation helps predict Y if we know X1 and X2

#🟢 Predict on validation and test sets
val_pred = model.predict(X_val)
test_pred = model.predict(X_test)
#👉 Predicts Y values using the model
#👉 These will be compared with actual values to check performance

#🟢 Calculate RMSE and R2 scores
val_rmse = mean_squared_error(y_val, val_pred, squared=False)
val_r2 = r2_score(y_val, val_pred)

test_rmse = mean_squared_error(y_test, test_pred, squared=False)
test_r2 = r2_score(y_test, test_pred)
#👉 RMSE (Root Mean Squared Error) tells average error — lower is better
#👉 R2 (R-squared score) tells accuracy — closer to 1 is better
#👉 Example:
#    RMSE = 5 → predictions are ~5 units off on average
#    R2 = 0.92 → model is 92% accurate

#🟢 Correlation matrix
correlation = df.corr()
#👉 Shows strength of linear relationships between columns
#👉 Example:
#       X1     X2     Y
# X1   1.00   0.85   0.92
# X2   0.85   1.00   0.88
# Y    0.92   0.88   1.00
#👉 This means X1 and X2 both affect Y positively and strongly

#🟢 Plot the data points
plt.figure(figsize=(10, 5))
plt.scatter(df['X1'], df['Y'], label='X1 vs Y', alpha=0.7)
plt.scatter(df['X2'], df['Y'], label='X2 vs Y', alpha=0.7)
plt.title('Scatter Plot')
plt.xlabel('X1 and X2')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
#👉 Visualizes the relation between X1-Y and X2-Y
#👉 Helps see trends, patterns, or outliers in the data

#🟢 Predict using user input
def predict_manual(x1, x2):
    return model.predict(np.array([[x1, x2]]))[0]
#👉 Lets you manually input X1 and X2 to get predicted Y
#👉 Example:
#    predict_manual(50, 100) → returns a predicted Y value

#🟢 Final output
print("📌 Best Fit Equation:", best_fit_eq)
print("✅ Validation RMSE:", val_rmse)
print("✅ Validation R2:", val_r2)
print("✅ Test RMSE:", test_rmse)
print("✅ Test R2:", test_r2)
print("📊 Correlation Matrix:\n", correlation)
print("🎯 Example prediction for X1=50, X2=100:", predict_manual(50, 100))
#👉 Shows all key results:
#   - Regression equation
#   - Errors and accuracy
#   - Correlation table
#   - Sample prediction from manual values