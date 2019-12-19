from django.urls import reverse
from rest_framework import status

from authentication.models import User
from tests.base import BaseTestCase
from tests.sample_data.authentication import user_1


class AuthTests(BaseTestCase):
    def test_sign_up(self):
        """
        Ensure user can create account
        """
        response = self.signup_user(user_1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_account(self):
        """
        Ensure duplicate accounts are handled
        """
        self.signup_user(user_1)
        response = self.signup_user(user_1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
