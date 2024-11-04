# - user can deposit 
# - user can withdraw
from modules.atm import Atm
from modules.transaction import Transaction
from enums.transaction_type import TransactionType
from modules.accounts import Account

def get_account_details(atm, id):
    return atm.get_account_by_id(id)

def main():

    account = Account(123, "Vish")
    atm =  Atm(10000, "Jodhpur", "SBI" , [account])

    

    while True:
    
        try:
            acc_number  = int(input("Enter your account number  - "))
            account =  get_account_details(atm, acc_number)

            if account is not None:
                print(f'Hello {account.name}')
                while True:
                    print('\n To withdraw cash press - 1 \n To deposit cash press -2 \n TO EXIIT - 3 \n check balance - 4 ')
                    i = int(input("Enter here - "))

                    if i == 1:
                        amount = int(input("Enter amount - "))
                        if amount > account.balance:
                            print(f"Sorry but your account balance is less than {amount}")
                        else:
                            transaction = Transaction(amount, account.id, TransactionType.DEBIT)
                            account.add_transaction(transaction)
                    elif i == 2 :
                        amount = int(input("Enter amount - "))
                        transaction = Transaction(amount, account.id, TransactionType.CREDIT)
                        account.add_transaction(transaction)

                    elif i == 3:
                        break

                    elif i == 4:
                        print(f"account balce is - {account.balance}")
                    else:
                        print("Invalid input")

            else:
                print("Account does not exist")

        
        except ValueError:
            print("Enter valid input")

    

if __name__ == "__main__":
    main()