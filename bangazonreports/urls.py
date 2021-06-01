from django.urls import path
from .views import favorite_sellers_by_user

urlpatterns = [
    path('reports/customerfavorites', favorite_sellers_by_user),
]