class Bank:
    def __init__(self,account_number,balance):
        self.balance= balance
        self.__account_number=account_number
    def deposit(self,amount):
        self.balance=self.balance+amount
    def check_balance(self):
        print(self.balance)
    def show_accountnumber(self,isauth):
      if  isauth==True:
        print(self.__account_number)
      else:
          print("not allowed")




axis=Bank("1234",100)
axis.deposit(200)
axis.check_balance()
axis.show_accountnumber(True)

