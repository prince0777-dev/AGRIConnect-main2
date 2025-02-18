import joblib
import numpy as np

# Load trained model
model = joblib.load("random_forest_model.pkl")

def predict_price(features: list):
    """Predicts the price based on input features"""
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)
    return round(prediction[0], 2)  # Return rounded prediction
