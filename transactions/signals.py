from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models import Transaction
from account.models import Account


@receiver(post_save, sender=Transaction)
def update_account_balance(sender, **kwargs):
    """
    Update account if transaction successful.
    """
    transaction = kwargs['instance']
    if not kwargs['created'] and transaction.status == 'success':
        account = transaction.account
        account.balance = transaction.new_balance
        account.save()
