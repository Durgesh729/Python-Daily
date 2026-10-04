class BankAccount:
    def __init__(self,initial_balance=0):
        self.__balance=initial_balance if initial_balance > 0 else 0
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            return "Error: Deposit amount must be positive."
    def withdraw(self, amount):
        if amount <= 0:
            return "Error: Withdrawal amount must be positive."
        elif amount > self.__balance:
            return "Error: Insufficient funds."
        else:
            self.__balance -= amount
            return f"new balance: {self.__balance}"
    def get_balance(self):
        return f"balance: {self.__balance}"
    
Account=BankAccount(100)
deposit_money=int(input("Enter money to deposit: "))
print(Account.deposit(deposit_money))
withdraw_money=int(input("Enter money to withdraw: "))
print(Account.withdraw(withdraw_money))
print(Account.get_balance())
