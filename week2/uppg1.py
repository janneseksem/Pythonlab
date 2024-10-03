class Bankkonto:
    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
           print("Your amount cannot be negative")
            
        else:
            self.balance += amount
            
    def withdraw(self, amount):
        if amount < 0:
            print("Your amount cannot be negative")
            
        else:
            self.balance -= amount
    
    def display_balance(self):
        return (f"Your account balance is {self.balance} SEK")

bank1 = Bankkonto("Daniel", 100)
print(bank1.display_balance())

bank1.deposit(300)
print(bank1.display_balance())

bank1.withdraw(160)
print(bank1.display_balance())
