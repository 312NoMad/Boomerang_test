from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import *

User = get_user_model()


class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.sample_product = Product.objects.create(
            name='Test Product',
            description='Lorem ipsum dolor sit amet',
            price=42,
        )

    def test_list_products(self):
        url = reverse('product-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            'name': 'Test Product 2',
            'description': 'Lorem ipsum dolor sit amet',
            'price': 42,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_product(self):
        url = reverse('product-detail', kwargs={'pk': self.sample_product.pk})
        data = {
            'name': 'Test Product Update',
            'description': 'Test Product Update',
            'price': 12,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_product = Product.objects.get(pk=self.sample_product.pk)
        self.assertEqual(updated_product.name, data.get('name'))
        self.assertEqual(updated_product.price, data.get('price'))
        self.assertEqual(updated_product.description, data.get('description'))


