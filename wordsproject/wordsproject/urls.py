from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('converter.urls')),  # This tells Django to use your app's urls.py for root URL
]
