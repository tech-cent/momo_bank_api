from mtnmomo.disbursement import Disbursement

from utils.payment.operation import Operation


class Withdraw(Operation):
    """
    Bank to mobile money transaction.
    """

    name = 'Withdraw'

    def __init__(self, phone_number, amount, trans_id):
        super().__init__(phone_number, amount, trans_id)

    def execute(self):
        """
        Witdraw from account
        """
        client = Disbursement(self.config)
        transaction_ref = client.transfer(
            amount=self.amount, mobile=self.phone_number,
            external_id=self.trans_id, payee_note="dd",
            payer_message="dd", currency="EUR")
        transaction_status = client.getTransactionStatus(
            transaction_ref['transaction_ref']
        )
        return transaction_status
