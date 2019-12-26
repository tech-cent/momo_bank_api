from django.urls import reverse
from rest_framework.test import APITestCase

from account.models import Account
from bank.models import Bank


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

    @staticmethod
    def create_bank(bank_details):
        """
        creates an instance of Bank
        using the given bank details which is a dictionary
        """
        return Bank.objects.create(**bank_details)

    def create_account(self, account_details, token, url):
        """
        create an account by posting the create account endpoint
        """
        self.add_token(token)
        return self.client.post(url, account_details, format='json')