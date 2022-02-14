class bankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        bankAccount.accounts.append(self)
    def deposit (self, amount):
        self.balance += amount
        return self

    def withdraw (self, amount):
        if bankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient Funds: Charging $5 fee")
        return self

    def display_account_info (self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += (self.balance * self.int_rate)
            return self

    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    @classmethod
    def allInfo (cls):
        for account in cls.accounts: 
            account.display_account_info()
        
savings = bankAccount(.02,500)
savings.deposit(200).deposit(400).deposit(150).withdraw(500).yield_interest().display_account_info()
checking = bankAccount(.01, 500)
checking.deposit(200).deposit(200).withdraw(300).withdraw(200).withdraw(175).withdraw(300).yield_interest().display_account_info()

bankAccount.allInfo()