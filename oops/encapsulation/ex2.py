class BankAccount:
    def __init__(self,account_number,balance):
        if len(account_number) == 10 and account_number.isdigit():
            self.__account_number=account_number
            self.__balance=balance
        else:
            raise ValueError("Invalid Account Number")
    
    def getBalance(self):
        return f"Balance: ${self.__balance}"
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            return f"Updated Balance: ${self.__balance}"
        else:
            print("Invalid Amount")
    
    def withdraw(self,amount_to_withdraw):
        if amount_to_withdraw <= self.__balance:
            self.__balance-=amount_to_withdraw
            return f"Updated Balance: ${self.__balance}"
        else:
            raise ValueError("Not Allowed")
    
    def account_info(self):
        return f"xxxxxx{self.__account_number[-4:]}"
    
s=BankAccount("1234567890",10)
print(s._BankAccount__balance)