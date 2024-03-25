from rest_framework import serializers

from .models import *


__all__ = [
    'OrderSerializer',
    'CartSerializer',
    'CartItemSerializer',
    'OrderItemSerializer',
]


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('product', 'quantity', 'cost')


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'cost')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'status', 'description', 'user', 'order_items', 'total_cost', 'created_at', 'updated_at')


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart_items', 'total_cost', 'created_at', 'updated_at')
