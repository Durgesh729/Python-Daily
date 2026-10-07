class SavingAccount:
    Bank_Name="SBI"
    def __init__(self,holder_name,balance):
        self.holder_name=holder_name
        self.balance=balance
    def display(self):
        return f"{self.holder_name}:{self.balance}"
        
class CurrentAccount(SavingAccount):
    Bank_Name="Bank of India"
    def __init__(self, holder_name, balance):
        super().__init__(holder_name, balance)

saving=SavingAccount("Durgesh",20)
saving1=SavingAccount("kishor",999999999)
Current=CurrentAccount("Durgesh",99999999)
Current1=CurrentAccount("Kishor",20)
print(f"Bank Name: {saving.Bank_Name}\n{saving.display()}\n{saving1.display()}\nBank Name: {Current.Bank_Name}\n{Current.display()}\n{Current1.display()}")
