from mtnmomo.collection import Collection

from utils.payment.operation import Operation


class Deposit(Operation):
    """
    Handles depositing money to account by
    send a withdrawal request to user's number.
    """

    name = 'Deposit'

    def __init__(self, phone_number, amount, trans_id):
        super().__init__(phone_number, amount, trans_id)

    def execute(self):
        """
        Deposit money to account
        """
        client = Collection(self.config)
        transaction_ref = client.requestToPay(
            mobile=self.phone_number,
            amount=self.amount,
            external_id=self.trans_id,
            payee_note="dd",
            payer_message="dd",
            currency="EUR"
        )
        transaction_status = client.getTransactionStatus(
            transaction_ref['transaction_ref'])
        return transaction_status
