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
