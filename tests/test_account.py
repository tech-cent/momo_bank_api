from django.urls import reverse
from rest_framework import status

from account.models import Account
from tests.base import BaseTestCase
from tests.sample_data.account import account_1, incomplete_account
from tests.sample_data.authentication import user_1, user_1_login, user_2, user_2_login
from tests.sample_data.bank import bank_1


class AccountTestCase(BaseTestCase):
    """
    tests on the account entity
    """

    def setUp(self):
        self.signup_user(user_1)
        self.signup_user(user_2)
        self.token = self.login_user(user_1_login)
        self.token_2 = self.login_user(user_2_login)
        self.base_url = reverse('account:base')
        self.bank = self.create_bank(bank_1)

    def test_create_account(self):
        """
        Ensure logged in user can create account
        """
        response = self.create_account(
            account_1(self.bank), self.token, self.base_url)
        accounts = Account.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(len(accounts), 0)

    def test_create_incomplete_account(self):
        """
        Ensure a missing field results in a 400 error.
        """
        response = self.create_account(
            incomplete_account(self.bank), self.token, self.base_url)
        accounts = Account.objects.all()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_accounts(self):
        """
        Endpoint should return a list of accounts
        """
        self.add_token(self.token)
        self.create_account(account_1(self.bank), self.token, self.base_url)
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_single_account(self):
        """
        Endpoint should return a single object
        """
        account = self.create_account(
            account_1(self.bank), self.token, self.base_url)
        url = reverse('account:detail', kwargs={'pk': account.data['id']})
        self.add_token(self.token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_access_to_account(self):
        """
        User should not be able to check account
        belonging to another user
        """
        account = self.create_account(
            account_1(self.bank), self.token, self.base_url)
        url = reverse('account:detail', kwargs={'pk': account.data['id']})
        self.add_token(self.token_2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
