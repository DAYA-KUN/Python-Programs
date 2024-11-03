class BankAccount:

    def __init__(self,owner,balance=0):
        self.owner=owner
        self.__balance=balance # Private Variable : __variablename # Protected variable : _variablename

    def deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return f"The Balance is {self.__balance}"
    
    def get_owner(self):
        return f"The Owner of this account is {self.owner}"
    
account1=BankAccount("Daya")
account1.deposit(500)
print(account1.get_balance())
print(account1.get_owner())

