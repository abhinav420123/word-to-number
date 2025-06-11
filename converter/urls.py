from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This maps root URL to your index view
]
