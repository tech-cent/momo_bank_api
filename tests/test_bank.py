from django.urls import reverse
from rest_framework import status

from bank.models import Bank
from tests.base import BaseTestCase
from tests.sample_data.authentication import user_1, user_1_login
from tests.sample_data.bank import bank_1, incomplete_bank


class BankTestCase(BaseTestCase):
    """
    tests on the bank entity
    """

    def setUp(self):
        self.signup_user(user_1)
        self.token = self.login_user(user_1_login)

    def test_create_bank(self):
        """
        Ensure logged in user can create bank
        """
        url = reverse('bank:base')
        self.add_token(self.token)
        response = self.client.post(url, bank_1, format='json')
        bank = Bank.objects.get(name=bank_1['name'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bank.tin, bank_1['tin'])
        self.assertEqual(str(bank), f"Bank Name is :{bank_1['name']}")

    def test_duplicate_bank(self):
        """
        Ensure duplicate bank name results in a 400 error.
        """
        url = reverse('bank:base')
        self.add_token(self.token)
        self.client.post(url, bank_1, format='json')
        response = self.client.post(url, bank_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_required_fields(self):
        """
        Ensure missing fields are caught
        """
        url = reverse('bank:base')
        self.add_token(self.token)
        response = self.client.post(url, incomplete_bank, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_banks(self):
        """
        Endpoint should return a list
        """
        url = reverse('bank:base')
        self.add_token(self.token)
        self.client.post(url, bank_1, format='json')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
