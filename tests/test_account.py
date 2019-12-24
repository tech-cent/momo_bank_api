from django.urls import reverse
from rest_framework import status

from account.models import Account
from tests.base import BaseTestCase
from tests.sample_data.authentication import user_1, user_1_login
from tests.sample_data.account import account_1


class AccountTestCase(BaseTestCase):
    """
    tests on the account entity
    """

    def setUp(self):
        self.signup_user(user_1)
        self.token = self.login_user(user_1_login)

    def test_create_account(self):
        """
        Ensure logged in user can create account
        """
        url = reverse('account:base')
        self.add_token(self.token)
        response = self.client.post(url, account_1(), format='json')
        accounts = Account.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(len(accounts), 0)
