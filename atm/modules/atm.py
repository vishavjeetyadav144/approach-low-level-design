class Atm:

    def __init__(self, cash , location , bank, accounts = []) -> None:
        self.available_cash = cash
        self.location = location 
        self.bank = bank
        self.accounts = accounts

    def get_atm_details(self):
        print(f'Location - {self.location}')
        print(f'Bank - {self.bank}')

    def get_account_by_id(self, id):

        account = None

        for acc in self.accounts:
            if acc.id == id:
                account = acc
                break

        return account

    