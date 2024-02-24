
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .views import OrderAPIView, OrderAPIAdminView, AddDataAPIView, DeleteDataAPIView
from .models import Order
from account.models import Customer
from product.models import Products
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.test import APIClient

class OrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='Avinash', password='Kumar@2501')
        self.customer = Customer.objects.create(user=self.user)
        self.product = Products.objects.create(name='Test Product')

    def test_Order_api_view_get(self):
        # Perform login to get authentication token
        response = self.client.post('/api/token/', {'username': 'Avinash', 'password': 'Kumar@2501'})
        self.assertEqual(response.status_code, 200)
        token = response.data['access']
        print(response.data)

        # Set Authorization header with the token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        print("--------------------------------------------------")

        # Test retrieving all Orders
        
        response = self.client.get('http://127.0.0.1:8000/order/')
        self.assertEqual(response.status_code, 200)
        print("--------------------------------------------------")
        # Test handling when the Order does not exist
        response = self.client.get('http://127.0.0.1:8000/order/100/')
        self.assertEqual(response.status_code, 404)
