from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

from django.contrib.auth import get_user_model


User = get_user_model()


class AccountTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@localhost.com',
            password='testpassword',
            first_name='',
            last_name=''
        )

    def test_signup(self):
        data1 = {
            'username': 'testuser123',
            'email': 'test@localhost.com',
            'password': 'testpassword123',
            'password_confirm': 'testpassword123',
            'first_name': '',
            'last_name': ''
        }
        data2 = {
            'username': 'newuser1',
            'email': 'testuser@localhost.com',
            'password': 'testpassword123',
            'password_confirm': 'testpassword123',
            'first_name': '',
            'last_name': ''
        }
        url = reverse('signup')

        response1 = self.client.post(url, data1, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)

        response2 = self.client.post(url, data2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@localhost.com',
            'password': 'testpassword',
            'first_name': '',
            'last_name': ''
        }
        url = reverse('login')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data.get('refresh')

    def test_refresh(self):
        data = {
            'refresh': self.test_signin()
        }
        url = reverse('refresh')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        refresh_token = self.test_signin()
        data = {
            'refresh': refresh_token
        }
        url = reverse('logout')
        url2 = reverse('refresh')

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response2 = self.client.post(url2, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response2.data, {"detail": "Token is blacklisted", "code": "token_not_valid"})
