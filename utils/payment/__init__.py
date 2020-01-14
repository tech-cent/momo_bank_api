from .driver import handle_operation


class Payment():

    def __init__(self, phone_number, amount, trans_id, type):
        self.phone_number = phone_number
        self.amount = amount
        self.trans_id = trans_id
        self.type = type

    def execute(self):
        """mobile money to bank transfer"""
        return handle_operation(
            self.type, self.phone_number, self.amount, self.trans_id)
