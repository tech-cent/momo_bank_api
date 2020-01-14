import os
from abc import ABC, abstractmethod, abstractproperty

from dotenv import load_dotenv

load_dotenv()

config = {
    "ENVIRONMENT": os.environ.get("ENVIRONMENT"),
    "CALLBACK_HOST": os.environ.get("CALLBACK_HOST"),
    "COLLECTION_PRIMARY_KEY": os.environ.get("COLLECTION_PRIMARY_KEY"),
    "COLLECTION_USER_ID": os.environ.get("COLLECTION_USER_ID"),
    "COLLECTION_API_SECRET": os.environ.get("COLLECTION_API_SECRET"),
    "DISBURSEMENT_USER_ID": os.environ.get("DISBURSEMENT_USER_ID"),
    "DISBURSEMENT_API_SECRET": os.environ.get("DISBURSEMENT_API_SECRET"),
    "DISBURSEMENT_PRIMARY_KEY": os.environ.get("DISBURSEMENT_PRIMARY_KEY")
}


class Operation(ABC):
    """
    Abstract class for all mobile money transactions
    """

    config = config

    @abstractproperty
    def name(self):
        pass

    def __init__(self, phone_number, amount, trans_id):
        self.phone_number = phone_number
        self.amount = amount
        self.trans_id = trans_id
        super().__init__()

    @abstractmethod
    def execute(self):
        pass
