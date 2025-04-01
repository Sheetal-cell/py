class BankAccount:
    def __init__(self, owner):
        self.owner, self.balance, self.transactions = owner, 0, []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"+${amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"-${amount}")
        else:
            print("Insufficient funds.")
    
    def check_balance(self):
        print(f"Balance: ${self.balance}")
    
    def print_statement(self):
        print("\nStatement:", *self.transactions, f"Balance: ${self.balance}", sep="\n")

acc = BankAccount("John Doe")
acc.deposit(100)
acc.withdraw(30)
acc.check_balance()
acc.print_statement()
