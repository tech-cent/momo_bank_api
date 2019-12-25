from django.urls import reverse
from rest_framework import status

from account.models import Account
from tests.base import BaseTestCase
from tests.sample_data.account import (account_1, create_bank,
                                       incomplete_account)
from tests.sample_data.authentication import user_1, user_1_login
from tests.sample_data.bank import bank_1


class AccountTestCase(BaseTestCase):
    """
    tests on the account entity
    """

    def setUp(self):
        self.signup_user(user_1)
        self.token = self.login_user(user_1_login)
        self.base_url = reverse('account:base')
        self.bank = create_bank(bank_1)

    def test_create_account(self):
        """
        Ensure logged in user can create account
        """
        self.add_token(self.token)
        response = self.client.post(self.base_url, account_1(self.bank), format='json')
        accounts = Account.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(len(accounts), 0)

    def test_create_incomplete_account(self):
        """
        Ensure a missing field results in a 400 error.
        """
        self.add_token(self.token)
        response = self.client.post(self.base_url, incomplete_account(self.bank), format='json')
        accounts = Account.objects.all()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(accounts), 0)

    def test_get_accounts(self):
        """
        Endpoint should return a list of accounts
        """
        self.add_token(self.token)
        self.client.post(self.base_url, account_1(self.bank), format='json')
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
