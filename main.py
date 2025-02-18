from fastapi import FastAPI
from pydantic import BaseModel
from predictor import predict_price

app = FastAPI()

# Request body model
class PricePredictionRequest(BaseModel):
    feature1: float
    feature2: float
    feature3: float  # Add more features as needed

@app.post("/predict-price")
async def predict_price_api(request: PricePredictionRequest):
    features = [request.feature1, request.feature2, request.feature3]  # Modify based on actual features
    price = predict_price(features)
    return {"predicted_price": price}
