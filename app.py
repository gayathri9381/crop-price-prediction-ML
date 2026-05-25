# Crop Price Prediction using Machine Learning

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# -----------------------------------
# Step 1: Create Sample Dataset
# -----------------------------------

data = {
    'Rainfall': [120, 140, 100, 130, 150, 110, 170, 160, 180, 190],
    'Temperature': [30, 32, 28, 31, 35, 29, 36, 34, 37, 38],
    'Demand': [200, 250, 180, 220, 300, 210, 320, 310, 350, 370],
    'Price': [1800, 2000, 1700, 1900, 2500, 1850, 2700, 2600, 2900, 3000]
}

df = pd.DataFrame(data)

print("Dataset Preview:")
print(df.head())

# -----------------------------------
# Step 2: Define Features and Target
# -----------------------------------

X = df[['Rainfall', 'Temperature', 'Demand']]
y = df['Price']

# -----------------------------------
# Step 3: Split Dataset
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------------
# Step 4: Train Model
# -----------------------------------

model = RandomForestRegressor(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

# -----------------------------------
# Step 5: Predictions
# -----------------------------------

predictions = model.predict(X_test)

# -----------------------------------
# Step 6: Model Evaluation
# -----------------------------------

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation:")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# -----------------------------------
# Step 7: Predict New Crop Price
# -----------------------------------

new_data = [[145, 33, 280]]

predicted_price = model.predict(new_data)

print("\nPredicted Crop Price: ₹", round(predicted_price[0], 2), "per quintal")

# -----------------------------------
# Step 8: Visualization
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.plot(df['Price'], marker='o')

plt.title("Crop Price Trend Analysis")
plt.xlabel("Data Index")
plt.ylabel("Crop Price (₹)")

plt.grid(True)

plt.show()
