from django.db import models
from authentication.models import User


class Bank(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tin = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"Bank Name is :{self.name}"
