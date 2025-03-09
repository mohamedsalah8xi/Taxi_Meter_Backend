from django.urls import path
from django.http import JsonResponse
from .views import trip_api

def test_api(request):
    return JsonResponse({"message": "Taxi Meter API is working!"})

def home(request):
    return JsonResponse({"message": "Welcome to Taxi Meter API!"})

urlpatterns = [
    path("", home, name="home"),
    path("test/", test_api, name="test_api"),
    path("trips/", trip_api, name="trip_api"),
]