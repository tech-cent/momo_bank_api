from bank.models import Bank
from tests.sample_data.bank import bank_1


def account_1():
    """
    Creates sample account data.
    """
    bank = Bank.objects.create(**bank_1)
    account_dict = {
        "type":"default",
        "bank":bank.id
    }
    return account_dict
