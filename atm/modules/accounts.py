from enums.transaction_type import TransactionType

class Account:

    def __init__(self, id, name , balance = 100) -> None:
        self.id = id
        self.name = name
        self.balance = balance
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

        print(transaction.type)
        if transaction.type == TransactionType.CREDIT:
            self.balance += transaction.amount
        elif transaction.type == TransactionType.DEBIT:
            self.balance -= transaction.amount

    
        
