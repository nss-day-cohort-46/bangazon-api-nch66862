from django.urls import path
from .views import favorite_sellers_by_customer, incomplete_orders

urlpatterns = [
    path('reports/customerfavorites', favorite_sellers_by_customer),
    path('reports/incomplete-orders', incomplete_orders),
]