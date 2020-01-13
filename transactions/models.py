from django.db import models

from account.models import Account
from authentication.models import User


class Transaction(models.Model):
    type = models.CharField(max_length=50)
    amount = models.IntegerField()
    prev_balance = models.IntegerField()
    new_balance = models.IntegerField()
    status = models.CharField(max_length=50, default="new")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def calculate_new_balance(self):
        type = self.type.lower()
        if type == 'deposit':
            self.new_balance = self.prev_balance + self.amount
        if type == 'withdraw':
            self.new_balance = self.prev_balance - self.amount
