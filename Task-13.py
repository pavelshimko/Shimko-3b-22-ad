class BankAccount():
    owner_name = 'Ivan'
    account_number = 'Ivanov'
    balance = 10000

    def add_money(self, amount):
        self.balance += amount

    def substract_money(self, amount):
        self.balance -= amount

bank_acc = BankAccount()
bank_acc.add_money(2000)
bank_acc.substract_money(1000)
print(bank_acc.balance)