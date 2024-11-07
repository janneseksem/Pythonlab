'''
Skriv en klass Bankkonto

    Den ska ha attributen owner och dess saldo/balance kommer initialt vara 0.
    Skapa metoder såsom deposit(amount) för att lägga till pengar till kontot samt withdraw(amount) för att ta ut pengar från kontot. Se också till att saldot ej kan bli negativ!
    Skapa en metod display_balance() för som printar kontots nuvarande saldo.
'''

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
