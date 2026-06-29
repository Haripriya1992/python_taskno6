# Base Class
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # encapsulation
        self.__balance = balance


    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. New Balance: ₹{self.__balance}")


# Subclass 1 - Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest Amount: ₹{interest}")
        return interest


# Subclass 2 - Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, min_balance=1000):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.get_balance() - amount < self.min_balance:
            print(f"Cannot withdraw! Minimum balance ₹{self.min_balance} must be maintained.")
        else:
            super().withdraw(amount)


print("=== Savings Account ===")
sa = SavingsAccount("SA001", 5000, 0.05)
sa.deposit(2000)
sa.withdraw(1000)
sa.calculate_interest()

print("\n=== Current Account ===")
ca = CurrentAccount("CA001", 5000, 1000)
ca.deposit(3000)
ca.withdraw(6500)  # Should fail - below min balance
ca.withdraw(2000)  # Should work