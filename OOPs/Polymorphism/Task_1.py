"""
1. Banking System:
   Problem Statement: Implement a banking system where customers can perform various transactions such as deposit, withdrawal, and transfer. The system should support different methods for each transaction type, allowing flexibility in parameter types. For example, the deposit method should accept an account number and either a single amount or a list of amounts to be deposited.
"""

class BankingSystem:
        # def deposit_single(self, account_number, amount: int):
        #         # Deposit a single amount to the specified account
        #         print(f"Depositing {amount} to account {account_number}")

        def deposit_multiple(self, account_number, amounts):
                # Deposit a list of amounts to the specified account
                for amount in amounts:
                        print(f"Depositing {amount} to account {account_number}")

        def withdraw(self, account_number, amount):
                # Withdraw a single amount from the specified account
                print(f"Withdrawing {amount} from account {account_number}")

        def transfer(self, from_account, to_account, amount):
                # Transfer a single amount from one account to another
                print(f"Transferring {amount} from account {from_account} to account {to_account}")


bank = BankingSystem()

bank.deposit(123456, [1000])  # Depositing 1000 to account 123456

bank.deposit(123456, [1000, 2000, 3000])  # Depositing 1000, 2000, 3000 to account 123456

bank.withdraw(123456, 1000)  # Withdrawing 1000 from account 123456

bank.transfer(123456, 654321, 1000)  # Transferring 1000 from account 123456 to account 654321