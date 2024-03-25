from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from apps.product.models import Product

from .models import CartItem, Order, Cart

User = get_user_model()


class CartTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name='Test Product', price=100)

    def test_add_to_cart(self):
        # print('\n\n\n', self.product.id, '\n\n\n')
        url = reverse('add-to-cart')
        data = {'product': self.product.id, 'quantity': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # print('\n\n\n', CartItem.objects.all(), '\n\n\n')
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(CartItem.objects.get().product.id, self.product.id)

    def test_create_order(self):
        self.test_add_to_cart()
        url = reverse('create-order')
        response = self.client.post(url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().order_items.count(), 1)
        self.assertEqual(Cart.objects.get(user=self.user).cart_items.count(), 0)

