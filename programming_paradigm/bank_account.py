# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to account balance."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Subtract amount from account balance if sufficient funds exist.
        Returns True if withdrawal succeeds, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance with 2 decimal places."""
        print(f"Current Balance: ${self.account_balance:.2f}")
