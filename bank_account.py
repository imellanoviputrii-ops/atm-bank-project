# Berisi class BankAccount,class yang menyimpan saldo

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print("Deposit berhasil")


    def withdraw(self, amount):

        if amount > self.balance:
            print("Saldo tidak cukup")

        else:
            self.balance -= amount
            print("Withdraw berhasil")


    def check_balance(self):
        print("Saldo sekarang:", self.balance)