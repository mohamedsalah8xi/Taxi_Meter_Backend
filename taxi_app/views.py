from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Trip  # تأكد من أن اسم التطبيق صحيح

@csrf_exempt
def trip_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            trip = Trip.objects.create(
                start_location=data.get("start_location"),
                end_location=data.get("end_location"),
                distance=data.get("distance"),
                fare=data.get("fare"),
            )
            return JsonResponse({"message": "Trip created successfully", "trip_id": trip.id}, status=201, json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400, json_dumps_params={'ensure_ascii': False})

    elif request.method == "GET":
        trips = list(Trip.objects.values())  # يحول جميع الرحلات إلى JSON
        return JsonResponse(trips, safe=False, json_dumps_params={'ensure_ascii': False})

    return JsonResponse({"error": "Method not allowed"}, status=405, json_dumps_params={'ensure_ascii': False})