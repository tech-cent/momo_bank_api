from django.urls import reverse
from rest_framework import status

from authentication.models import User
from account.models import Account
from tests.base import BaseTestCase
from tests.sample_data.authentication import (incomplete_user, user_1,
                                              user_1_login, user_duplicate_nin)


class AuthTests(BaseTestCase):
    def test_sign_up(self):
        """
        Ensure user can create account
        """
        response = self.signup_user(user_1)
        user = User.objects.get(phone_number=user_1['phone_number'])
        accounts = user.account_set.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(len(accounts), 0)

    def test_duplicate_account(self):
        """
        Ensure duplicate accounts are handled
        """
        self.signup_user(user_1)
        response = self.signup_user(user_1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, 'Number or NIN already exists')

    def test_duplicate_nin(self):
        """
        Ensure error message for already existing
        NIN
        """
        self.signup_user(user_1)
        response = self.signup_user(user_duplicate_nin)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, 'Number or NIN already exists')

    def test_incomplete_user(self):
        """
        Ensure 400 error if a field is missing
        """
        response = self.signup_user(incomplete_user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        """
        Ensure user can login using existing account
        """
        self.signup_user(user_1)
        url = reverse('authentication:login')
        response = self.client.post(url, user_1_login, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile(self):
        """
        Profile endpoint should return user's details
        """
        self.signup_user(user_1)
        token = self.login_user(user_1_login)
        self.add_token(token)
        url = reverse('authentication:profile')
        response = self.client.get(url)
        user_data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user_data['phone_number'], user_1['phone_number'])
