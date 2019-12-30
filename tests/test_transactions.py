from django.urls import reverse
from rest_framework import status

from account.models import Account
from authentication.models import User
from transactions.models import Transaction
from tests.base import BaseTestCase
from tests.sample_data.account import account_1
from tests.sample_data.authentication import user_1, user_1_login
from tests.sample_data.bank import bank_1
from tests.sample_data.transactions import sample_transaction


class TransactionsTestCase(BaseTestCase):
    """
    Tests on the transaction app
    """

    def setUp(self):
        self.signup_user(user_1)
        self.token = self.login_user(user_1_login)
        self.account_url = reverse('account:base')
        self.bank = self.create_bank(bank_1)
        self.account = self.create_account(account_1(self.bank), self.token, self.account_url)
 
    def test_deposit_transaction(self):
        """
        Ensure the transaction model proper increments balance
        """
        user = User.objects.get(phone_number=user_1_login['phone_number'])
        account = Account.objects.get(id=self.account.data['id'])
        transaction = Transaction()
        transaction.created_by = user
        transaction.account = account
        transaction.type = "deposit"
        transaction.amount = 10000
        transaction.prev_balance = account.balance
        transaction.calculate_new_balance()
        transaction.save()
        self.assertEqual(transaction.new_balance, 10000)

    def test_withdraw_transaction(self):
        """
        Ensure the transaction model handles withdrawal
        """
        user = User.objects.get(phone_number=user_1_login['phone_number'])
        account = Account.objects.get(id=self.account.data['id'])
        transaction = Transaction()
        transaction.created_by = user
        transaction.account = account
        transaction.type = "withdraw"
        transaction.amount = 5000
        transaction.prev_balance = 10000
        transaction.calculate_new_balance()
        transaction.save()
        self.assertEqual(transaction.new_balance, 5000)

    def test_post_transaction(self):
        """
        Ensure api can create a transaction given a post request
        """
        url = reverse('transactions:base')
        transaction = sample_transaction(self.account.data['id'], 'deposit', 10000)
        self.add_token(self.token)
        response = self.client.post(url, transaction, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'new')

    def test_bad_post_transaction(self):
        """
        Ensure bad post results in a 400 error
        """
        url = reverse('transactions:base')
        transaction = sample_transaction(self.account.data['id'], None, 10000)
        self.add_token(self.token)
        response = self.client.post(url, transaction, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_transactions(self):
        """
        Endpoint should return a list of transactions
        """
        url = reverse('transactions:base')
        transaction = sample_transaction(
            self.account.data['id'], 'deposit', 10000)
        self.add_token(self.token)
        self.client.post(url, transaction, format='json')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_account_transactions(self):
        """
        Endpoint should return a list of transactions belonging
        to a particular account
        """
        url = reverse('transactions:base')
        transaction = sample_transaction(
            self.account.data['id'], 'deposit', 10000)
        self.add_token(self.token)
        self.client.post(url, transaction, format='json')
        url = reverse(
            'account:transactions', kwargs={'pk': self.account.data['id']})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
