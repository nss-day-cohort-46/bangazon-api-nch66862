"""Module for generating favorite sellers by customer report"""
import sqlite3
from django.shortcuts import render
from bangazonapi.models import Customer, Favorite
from django.contrib.auth.models import User
from bangazonreports.views import Connection
from rest_framework import serializers

def favorite_sellers_by_customer(request):
    """Function to build an HTML report of favorite sellers by customer"""

    if request.method == 'GET':
        # Connect to project database
        favorite_sellers = {}
        customers = Customer.objects.all()
        favorites = Favorite.objects.all()
        for customer in customers:
            this_customers_favorites = favorites.filter(customer_id=customer.id)
            serialized_favorites = FavoritesSerializer(this_customers_favorites, many=True, context={'request': request}).data
            serialized_customer = CustomerSerializer(customer, many=False, context={'request': request}).data

        # Specify the Django template and provide data context
        template = 'customers/favorite_sellers_by_user.html'
        context = {
            'userevent_list': favorite_sellers
        }

        return render(request, template, context)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customer profile

    Arguments:
        serializers
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        depth = 1

class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for recommendation customers"""
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ('id', 'user',)

class FavoritesSerializer(serializers.ModelSerializer):
    """JSON serializer for recommendation customers"""
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ('id', 'user',)