from enums.transaction_status import TransactionStatus
import random
import string
from enums.transaction_type import TransactionType

class Transaction:

    def __init__(self, amount, account_id, type: TransactionType) -> None:
        self.id = ''.join(random.choices(string.digits, k = 10))
        self.amount = amount 
        self.account_id = account_id
        self.type = type
        self.status = TransactionStatus.PENDING

    def update_transaction_status(self, status):
        self.status = status