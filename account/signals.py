from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Account
from authentication.models import User
from bank.models import Bank


@receiver(post_save, sender=User)
def create_account(sender, **kwargs):
    """
    Create user account if a new user
    instance is saved
    """
    if kwargs['created']:
        user = kwargs['instance']
        bank = Bank.objects.get(name='Momo Bank')
        Account.objects.create(
            user=user, bank=bank, type='default', balance=0)
