def sample_transaction(account_id, transaction_type, amount):
    transaction_dic = {
        "account": account_id,
        "type": transaction_type,
        "amount": amount
    }
    return transaction_dic

update_transaction = {
    "status":"success"
}
