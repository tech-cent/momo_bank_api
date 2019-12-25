from bank.models import Bank


def create_bank(bank_details):
    """
    creates an instance of Bank
    using the given bank details which is a dictionary
    """
    return Bank.objects.create(**bank_details)

def account_1(bank):
    """
    Creates sample account data.
    Given a bank object.
    """
    account_dict = {
        "type":"default",
        "bank":bank.id
    }
    return account_dict

def incomplete_account(bank):
    """
    account with missing field,
    given a bank object.
    """
    account_dict = {
        "bank":bank.id
    }
    return account_dict
