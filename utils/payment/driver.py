from utils.payment.deposit import Deposit
from utils.payment.withdraw import Withdraw


def get_operations():
    """
    Create a dict containing the operations and their classes
    """
    operations = (Deposit, Withdraw)
    return dict([cls.name.lower(), cls] for cls in operations)


def parse_operations(operations, op_name, phone_number, amount, trans_id):
    """Select an operation and return it with arguments"""
    operation = operations.get(op_name)
    return operation(phone_number, amount, trans_id)


def handle_operation(op_name, phone_number, amount, trans_id):
    """handles execution of operation"""
    operations = get_operations()
    operation = parse_operations(
        operations, op_name, phone_number, amount, trans_id
    )
    return operation.execute()
