"""Module for generating favorite sellers by customer report"""
from django.shortcuts import render
from bangazonapi.models import Customer, Order
from django.contrib.auth.models import User
from rest_framework import serializers

def incomplete_orders(request):
    """Function to build an HTML report of favorite sellers by customer"""

    if request.method == 'GET':
        # Connect to project database
        incomplete_orders = []
        orders = Order.objects.filter(payment_type__isnull=True)
        for order in orders:
            serialized_order = OrderSerializer(order, many=False, context={'request': request}).data
            incomplete_orders.append(serialized_order)

        # Specify the Django template and provide data context
        template = 'orders/incomplete_orders.html'
        context = {
            'incomplete_orders': incomplete_orders
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

class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for recommendation customers"""
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ('id', 'user',)

class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for recommendation customers"""
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = ('id', 'customer', 'total_cost',)