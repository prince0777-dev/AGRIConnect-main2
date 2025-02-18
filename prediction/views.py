from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .predictor import predict_price

@csrf_exempt  # For simplicity in testing, disable CSRF verification (use with caution in production)
def predict_price_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            feature1 = data.get("feature1")
            feature2 = data.get("feature2")
            feature3 = data.get("feature3")
            
            if None in [feature1, feature2, feature3]:
                return JsonResponse({"error": "Missing required feature"}, status=400)
            
            # Get prediction
            features = [feature1, feature2, feature3]
            predicted_price = predict_price(features)
            
            return JsonResponse({"predicted_price": predicted_price})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=405)

