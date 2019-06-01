import json

# from django.urls import reverse

# from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase

from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from .models import ApiUser


class APIUserTest( APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('codetest.api.urls')),
    ]

    def setUp(self):
        self.create_url = reverse('api:create')
        self.login_url = reverse('api:login')

        self.data = {
            'first_name': "rex",
            'last_name': "test",
            'email': "rex.test@gmail.com",
            'password': "password123",
        }

        self.login_data = {
            'email': self.data['email'],
            'password': self.data['password']
        }

        self.user = ApiUser.objects.create(**self.data)


    def test_create_user(self):
        """
        Ensure we can create a new account object.
        """
        response = self.client.post(self.create_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_email(self):
        """
        Ensure it doesn't accept invalid email
        """
        # invalid email format
        self.data['email'] = "inval@id)@email.com"
        response = self.client.post(self.create_url, self.data, format='json')
        self.assertEqual(response.data['email'], ['Enter a valid email address.'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    
    def test_create_incomplete_data(self):
        """
        Ensure user creation doesn't accept null data
        """
        # invalid email format
        self.data['email'] = None
        self.data['password'] = None
        self.data['first_name'] = None
        self.data['last_name'] = None
        response = self.client.post(self.create_url, self.data, format='json')
        
        self.assertEqual(response.data['email'], ['This field may not be null.'])
        self.assertEqual(response.data['password'], ['This field may not be null.'])
        self.assertEqual(response.data['first_name'], ['This field may not be null.'])
        self.assertEqual(response.data['last_name'], ['This field may not be null.'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_created_user(self):
        """
        Ensure that the saved data is correct
        """
        self.assertEqual(self.user.first_name, self.data['first_name'])
        self.assertEqual(self.user.last_name, self.data['last_name'])
        self.assertEqual(self.user.email, self.data['email'])
        self.assertEqual(self.user.password, self.data['password'])

    def test_valid_login(self):
        """
        Ensure valid login
        """
        response = self.client.post(self.login_url, self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['token'])

    def test_invalid_login(self):
        """
        Ensure invalid login
        """
        self.login_data['password'] = 'wrongpassword'
        response = self.client.post(self.login_url, self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, 'invalid user')

    def test_incomplete_login(self):
        """
        Ensure incomplete login
        """
        self.login_data['password'] = None
        response = self.client.post(self.login_url, self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, 'invalid user')