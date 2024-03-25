from rest_framework.serializers import ModelSerializer

from .models import *


__all__ = [
    'ProductSerializer',
    'ReviewSerializer',
]


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'product', 'user', 'rating', 'description', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
