import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset (Replace 'your_dataset.csv' with your actual dataset file)
df = pd.read_csv("your_dataset.csv")

# Select features and target (modify according to your dataset)
features = ["feature1", "feature2", "feature3"]  # Adjust these columns
target = "price"

X = df[features]
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, y_pred)}")

# Save model
joblib.dump(model, "random_forest_model.pkl")
print("Model saved as random_forest_model.pkl")
