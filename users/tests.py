from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import User

# class SignUptest(APITestCase):
#     def test_registrtaion(self):
#         url = reverse("user_view")
#         user_data = {
#             "username" : "test",
#             "password" : "password"
#         }
#         response = self.client.post(url, user_data)
#         self.assertEqual(response.status_code, 200)



class LoginTest(APITestCase):
    def setUp(self):
        self.data = {'username':'testuser', 'password':'1234'}
        self.user = User.objects.create_user('testuser', '1234')
    
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        self.assertEqual(response.status_code, 200)
        print(response.data['access'])