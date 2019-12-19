from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user class to include phone number
    and change username field to phone_number
    """
    email = models.EmailField(null=True, blank=True, default='')
    username = models.CharField(null=True, blank=True, default='', unique=False, max_length=244)
    phone_number = models.CharField(unique=True, max_length=12)
    nin = models.CharField(unique=True, max_length=244)
    dob = models.DateField('date of birth')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'dob', 'nin']
