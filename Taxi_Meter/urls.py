from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("taxi_app.urls")),  # ربط المسارات من تطبيق taxi_app
]