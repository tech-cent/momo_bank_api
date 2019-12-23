from rest_framework.test import APITestCase
from django.urls import reverse


class BaseTestCase(APITestCase):
    """
    All helper methods
    """

    def signup_user(self, user):
        """
        Method signups user it is given
        by sending post request to signup
        endpoint
        """
        url = reverse('authentication:signup')
        return self.client.post(url, user, format='json')

    def add_token(self, token):
        """adds authentication credentials in the request header"""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def login_user(self, user):
        """
        logs in activated user and returns token
        """
        url = reverse('authentication:login')
        response = self.client.post(url, user, format='json')
        return response.data['access']
