# Define a class BankAccount with the following attributes and methods:
# Attributes:  account_number (string), account_holder (string), balance (float, initialized to 0.0(
# Methods: deposit(amount), withdraw(amount) , get_balance()
# - Create an instance of BankAccount, - Perform a deposit of $1000, - Perform a withdrawal of $500.
# - Print the current balance after each operation.
# - Define a subclass SavingsAccount that inherits from BankAccount and adds interest_rate Attribute
# and apply_interest() method that Applies interest to the balance based on the interest rate
# And Override print() method to print the current balance and rate.
# -  Create an instance of SavingsAccount , and call apply_interest() and print() functions.

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"amount of deposite is: {amount}$\nyour new balance is: {bank_account.get_balance()}$")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"amount of withdrawel is: {amount}$\nyour new balance is: {bank_account.get_balance()}$")
        else:
            print(f"!! insufficient funds !!\n your balance is {bank_account.get_balance()}$")
    def get_balance(self):
        return self.balance
    def get_accountholder(self):
        return self.account_holder
class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
    def print(self):
        print(f"Dear {self.account_holder}\nyour current balance is: {self.balance}$ with a rate of: {self.interest_rate * 100}%")
bank_account = BankAccount("1","Mohammad Said Fadel")
bank_account.deposit(1000)
bank_account.withdraw(500)
saving_account = SavingAccount("2", "Mohannad Issa", 2000, 0.05)
saving_account.apply_interest()
saving_account.print()
