from django.db import models
from authentication.models import User
from bank.models import Bank


class Account(models.Model):
    type = models.CharField(max_length=50)
    balance = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
