from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db import transaction

from apps.product.models import Product

from .models import *
from .serializers import *


class AddToCart(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)

        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity)
        cart_item.quantity += int(quantity)
        cart_item.save()


class CreateOrder(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        user = self.request.user
        cart = Cart.objects.get(user=user)
        with transaction.atomic():
            order = Order.objects.create(user=user, status='pending')
            for item in cart.cart_items.all():
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            cart.cart_items.all().delete()
        return Response(status=status.HTTP_201_CREATED, data=self.serializer_class(order).data)


class MyCartView(APIView):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        cart = Cart.objects.get(user=user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
